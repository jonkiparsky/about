# About Boston Python

Content and configuration for <https://about.bostonpython.com>, built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).

## Running the site locally

[Clone](https://help.github.com/en/articles/cloning-a-repository) (or [fork](https://help.github.com/en/articles/about-forks) then clone) this repo.

Install Ruby v2.6+ as explained in the [Jekyll docs](https://jekyllrb.com/docs/installation/) for your operating system (via [rbenv](https://github.com/rbenv/rbenv), for example).

Make sure both the installed Ruby version and RubyGems are on your path:

```
$ ruby -v
$ gem -v
```

Install [Bundler](https://bundler.io/):

```
$ gem install bundler
```

Install the gems to build the site:

```
$ bundle install
```

Build and serve the site:

```
$ bundle exec jekyll serve
```

View the site in a browser at <http://localhost:4000>.

## Developing the site

This site uses the [Hydeout](https://fongandrew.github.io/hydeout/) theme. Most of the site's structure and style come from the theme, so please have a look at the theme source code if you're interested in making any relevant changes.

To run Jekyll commands, use `bundle exec jekyll`.
