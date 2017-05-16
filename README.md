# beta-smgov

City of Santa Monica homepage on Jekyll

## Development Setup

This is a fairly standard [Jekyll][1] site using [Bundler][2] to manage gems.

Getting all of this working on Windows is *technically possible*, but it's a big
hassle. Jekyll recommends using Linux (e.g. Ubuntu) or OS X, and so do we.

1. Ensure you have the [correct version of Ruby][3] installed. A version manager
   such as [`rbenv`][4] is recommended (and will handle versioning automatically)

1. Clone the repo into a local directory

  ```
  $ git clone https://github.com/CityofSantaMonica/beta-smgov.git
  $ cloning into 'beta-smgov'...
  $ cd beta-smgov
  ```

1. Initialize the submodules

  ```
  $ git submodule update --init
  ```

1. Install gems and dependencies

  ```
  $ bundle install
  ```

1. Build and launch the website at http://localhost:4000. This also sets up a
   watch to automatically rebuild on changes

  ```
  $ bundle exec jekyll serve
  ```

[1]: http://jekyllrb.com/
[2]: http://bundler.io/
[3]: .ruby-version
[4]: https://github.com/rbenv/rbenv#basic-github-checkout
