"""
Install the requirements in requirements.txt in a virtualenv

To see the latest output for past-events/index.md, execute

    $ python add_meetup_events.py

To over-write with latest output, execute

    $ python add_meetup_events.py --rewrite
"""
import httpx
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime
from slugify import slugify
from jinja2 import Environment
import sys
from pathlib import Path


root = Path(__file__).parent.resolve()

# past events meetup URL
url = "https://www.meetup.com/bostonpython/events/past/"

# markdown file template saved under past-events
MD = """---
title: {{ title }}
sidebar_link: false
---

{{ event_date }}
{% for c in contents %}
{{ c }}
{% endfor %}

Meetup link: [{{ event_url }}]({{ event_url }})

[Back to Past Events Page](index.md)
"""

# list of all events which at the end are joined to contruct 
# the index.md file inside past-events folder
past_events = [
    "---",
    "title: Past Events",
    "sidebar_link: false",
    "---\n",
    "List of past events:\n",
]


if __name__ == "__main__":
    try:
        # by default this get only gets the 10 most recent events
        r = httpx.get(url)
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        raise

    soup = BeautifulSoup(r.content.decode('utf-8','ignore'), "lxml")

    datemap = defaultdict(list)

    # beautifulsoup finding the list of recent 10 events
    # mapping to defaultdict datemap
    lis = soup.find_all("li", {"class": "list-item border--none"})
    for li in lis:
        t = li.find("time")
        d = datetime.fromtimestamp(int(t["datetime"][:10]))
        year = d.year
        datemap[year].append(li)

    # get list of already existing event files under past-events 
    processed = Path('past-events').glob('**/*')
    processed_files = [x for x in processed if x.is_file()]

    # structure of data for existing_events
    # {
    #     2007: {
    #         datetime.date(2007, 5, 23): [
    #             ('The Cambridge Python May Meetup', '20070523-the-cambridge-python-may-meetup.md')
    #         ]
    #     }
    # }
    existing_events = defaultdict(lambda: defaultdict(list))

    # iterate all the files under past-events and populate
    # existing_events
    for p in processed_files:
        if p.name == "index.md":
            continue
        event_date = datetime.strptime(p.name.split("-")[0], "%Y%m%d").date()
        lines = p.read_text(encoding="utf-8").split("\n")
        title = None
        for line in lines:
            if line.startswith("title:"):
                _, title = line.split(": ")
                break
        existing_events[event_date.year][event_date].append((title, p.name))

    last_processed_year = max(existing_events.keys())
    max_processed_date = max(existing_events[last_processed_year])

    # now iterate over data downloaded from meetup and check whats not been processed
    # and saved under past-events
    for year, events in datemap.items():
        for event in events:
            link = event.find("a")
            url = link["href"]
            title = link.text
            parts = [part.strip() for part in title.split(":")]
            title = " - ".join(parts)
            if title == "Monday office hour":
                continue
            t = event.find("time")
            d = datetime.fromtimestamp(int(t["datetime"][:10]))
            if d.date() <= max_processed_date:
                continue
            name = slugify(title)
            filename = f"past-events/{d.strftime('%Y%m%d')}-{name}.md"
            location = event.find("div", {"class": "venueDisplay"})
            if not location:
                location = event.find("p", {"class": "venueDisplay"})
            attendees = event.find("li", {"class": "avatarRow--attendingCount"})
            try:
                count = attendees.text
            except:
                count = 0
            contents = event.find_all("p", {"class": "text--small"})
            new_contents = []
            for content in contents:
                if 'class' in content.attrs:
                    del content.attrs['class']
                if 'style' in content.attrs:
                    del content.attrs['style']
                new_contents.append(content)

            event_date = d.strftime("%B %d, %Y")
            mydict = {
                "title": title,
                "event_date": event_date,
                "location": location.text,
                "event_url": "https://www.meetup.com"+url,
                "contents": new_contents,
            }
            # write event file to past-events
            with open(filename, "w") as e:
                output = Environment().from_string(MD).render(**mydict).replace('\xa0', '')
                e.write(output)
                print(f"Write {filename}")
            # add to existing_events data structure
            existing_events[year][d.date()].append((title, f"{d.strftime('%Y%m%d')}-{name}.md"))        

    # Now go over all existing_events and construct past_events list
    for year in reversed(sorted(existing_events.keys())):
        past_events.append(f"- {year}")
        for dts in reversed(sorted(existing_events[year].keys())):
            for title, filename in sorted(existing_events[year][dts], key=lambda x:x[0]):
                past_events.append(f"    - [{title}]({filename}) ({dts:%m/%d/%Y})")

    # either print or over-write past-event/index.md file
    if "--rewrite" in sys.argv:
        index_file = root / "past-events" / "index.md"
        index_txt = "\n".join(past_events).strip()
        index_file.open("w").write(index_txt)
    else:
        print("\n".join(past_events))
