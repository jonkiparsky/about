# About Boston Python

Content and configuration for <https://about.bostonpython.com>, built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).

## Building the site locally

-   [Clone](https://help.github.com/en/articles/cloning-a-repository) (or [fork](https://help.github.com/en/articles/about-forks) then clone) this repo.
-   Install Ruby v2.6+ as explained in the [Jekyll docs](https://jekyllrb.com/docs/installation/) for your operating system (via [rbenv](https://github.com/rbenv/rbenv), for example).
-   Install the Bundler and Jekyll Ruby gems:
    -   Make sure both the installed Ruby version and RubyGems are on your path, as explained in the docs for [Jekyll](https://jekyllrb.com/docs/installation/) and [rbenv](https://github.com/rbenv/rbenv).
    -   Run `gem install bundler jekyll`.
-   Install the site: `cd BostonPython-about; bundle install`
-   Serve the site: `bundle exec jekyll serve`
-   View the site in a browser at [localhost:4000](http://localhost:4000).
