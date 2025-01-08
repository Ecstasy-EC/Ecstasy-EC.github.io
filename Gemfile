source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

gem "github-pages", "232", group: :jekyll_plugins

# If you want to use Jekyll native, uncomment the line below.
# To upgrade, run `bundle update`.

gem "jekyll"

# gem 'jekyll', "< 3.9.2"

# gem "wdm", "~> 0.1.0" if Gem.win_platform?
gem 'wdm', '~> 0.1.1', :install_if => Gem.win_platform?


# If you have any plugins, put them here!
group :jekyll_plugins do
  # gem "jekyll-archives"
  gem "jekyll-feed"
  gem 'jekyll-sitemap'
  gem 'hawkins'
end

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end


gem "kramdown", ">= 2.3.0"
gem "addressable", ">= 2.8.0"
gem "nokogiri", ">= 1.16.5"
gem "activesupport", ">= 6.1.7.5"

gem "webrick", "~> 1.9"
