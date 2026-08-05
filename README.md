A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note on Dependabot / security alerts

**Do not delete `Gemfile.lock`.** Deleting it throws away the pinned, known-good versions and re-resolves everything from scratch, which can silently reintroduce the very vulnerabilities you were trying to clear. Update the flagged gem in place instead:

```
bundle update <gem-name>        # e.g. bundle update nokogiri
bundle exec jekyll build        # confirm the site still builds
```

To check the whole lockfile against the Ruby advisory database:

```
gem install bundler-audit
bundle-audit check --update
```

Some fixes need a newer Ruby — e.g. `nokogiri >= 1.19` requires Ruby >= 3.2. Install one with `ruby-install ruby 3.4.10` and switch with `chruby` (see the MacOS section below).

Note that GitHub Pages builds this site remotely using its own gem versions and ignores your `Gemfile.lock` entirely, so these alerts affect **local development only** — not the published site.

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally in Ubuntu  (not on GitHub Pages but on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, do **not** delete `Gemfile.lock` (see the security note at the top) — check that your Ruby version is >= 3.2 first.
1. Run `bundle exec jekyll serve -l` to generate the HTML and serve it from `localhost:4000`; the local server will automatically rebuild and refresh the pages on change. (Don't use `jekyll liveserve` — the `hawkins` gem is broken with the pinned jekyll 3.10.0.)

## To run locally in Windows (not on GitHub Pages but on your own computer)

### Install Ruby & Devkit
1. Download and install Ruby and the associated Devkit from [RubyInstaller](https://rubyinstaller.org/downloads/).
1. Keep all options selected during the Ruby install.
1. Click the checkbox to run ridk install on the final screen of the Ruby install.
1. In the command window that appears, choose option 3 to install MSYS2 and the MINGW development toolchain.


### Install jekyll
1. Open an new command window and install Jekyll on Windows with the following command: `gem install jekyll bundler`.
1. Verify the install by issuing `jekyll -v` command.

### Start the liveserver
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, do **not** delete `Gemfile.lock` (see the security note at the top) — check that your Ruby version is >= 3.2 first.
1. Run `bundle add webrick` since webrick is no longer no longer bundled gems or standard librarie in Ruby>=3.0 (see [Ruby 3.0.0 Released](https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/)).
1. Run `bundle exec jekyll serve -l` to generate the HTML and serve it from `localhost:4000`; the local server will automatically rebuild and refresh the pages on change. (Don't use `jekyll liveserve` — the `hawkins` gem is broken with the pinned jekyll 3.10.0.) 

### Note
1. If you encounter the error `Permission denied - bind(2) for 127.0.0.1:4000`, please run your command prompt as administrator.
2. I encoutnered errors with a higher version of jekyll (e.g., 3.9.3). The jekyll version is set to `jekyll<3.9.2` in this repository (see also [Pin jekyll version <3.9.2](https://github.com/academicpages/academicpages.github.io/pull/944/commits/afefb7c37f89305063ce8fff39c4bf407d0120ac)).

## To run locally in MacOS (not on GitHub Pages but on your own computer)
### Install Chruby & Ruby-install
1. Run `brew install chruby ruby-install`.
2. Export chruby environment path into shell.
```
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
```
3. Install a supported Ruby by `ruby-install ruby 3.4.10` (compiles from source, takes a few minutes).
4. Change ruby version by `chruby ruby-3.4.10` and check by `ruby -v`.
5. To make it your shell default, add `chruby ruby-3.4.10` to `~/.zshrc` *after* the two `source` lines above, then open a new terminal.

### Install jekyll & bundler (optional)
1. Run `gem install jekyll bundler`.
2. Check by `jekyll -v` and `bundle -v`.

### Start live server
1. Change directory to the Website folder.
2. Run `bundle install` to install the pinned ruby dependencies. Do **not** delete `Gemfile.lock` first — see the security note at the top.
3. Serve the site:
```
bundle exec jekyll serve -l --config _config.yml,_config.dev.yml
```
4. Open `http://localhost:4000`. The server rebuilds and live-reloads the page on every file change. `Ctrl+C` stops it.

The `--config` flag layers [`_config.dev.yml`](_config.dev.yml) on top of the main config: it points `url` at `http://localhost:4000` (so internal links and SEO tags stay local instead of jumping to the live site), turns analytics off, and aims Disqus at a dummy shortname so local browsing doesn't touch real comments.

Note that `bundle exec jekyll liveserve` (from the `hawkins` gem) is **broken** with the pinned `jekyll 3.10.0` — it starts, but every page returns HTTP 500 with `NoMethodError: undefined method 'key?' for nil` from `hawkins-2.0.5/lib/hawkins/servlet.rb`. Use the `jekyll serve -l` form above instead; `-l` is jekyll's own built-in live reload and needs no extra gem.

### Note
1. Ruby >= 3.2 is **required**. The pinned `nokogiri` (`>= 1.19.4`, needed to clear known CVEs) does not support anything older, so the previously recommended `3.1.3` no longer works. This site is developed and tested on `3.4.10`.
2. Versions installed via `ruby-install` live in `~/.rubies`.
3. Uninstall a specific version of ruby: `rm -Rf ~/.rubies/ruby-3.1.3`
4. `webrick` is already declared in the `Gemfile`, so the `bundle add webrick` step in the Windows instructions above is not needed on MacOS.
5. If port 4000 is already in use, add `--port 4001` (or any free port).

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
