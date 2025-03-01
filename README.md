A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

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
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

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
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle add webrick` since webrick is no longer no longer bundled gems or standard librarie in Ruby>=3.0 (see [Ruby 3.0.0 Released](https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/)).
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change. 

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
3. Change ruby version by `chruby ruby-3.1.3` and check by `ruby -v`.

### Install jekyll & bundler (optional)
1. Run `gem install jekyll bundler`.
2. Check by `jekyll -v` and `bundle -v`.

### Start live server
1. Change directory to Website folder.
2. Remove locked Gemfile by `rm Gemfile.lock`
3. Generate new Gemfile by `bundle install`
4. Run `bundle add webrick` since webrick is no longer no longer bundled gems or standard librarie in Ruby>=3.0.
5. Run `bundle exec jekyll serve -l` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change. 

### Note
1. The ruby version `3.1.3` is a specific version that I found to work smoothly in both windows and MacOS. You could try other version using `ruby-install` and `chruby`.
2. The install version via `ruby-install` is in the directory `~/.rubies`.
3. Uninstall specific version of ruby: `rm -Rf ~/.rubies/ruby-3.1.3`

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
