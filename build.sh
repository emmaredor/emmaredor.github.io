#!/bin/bash
# Install Jekyll dependencies
bundle install

# Build the Jekyll site
JEKYLL_ENV=production bundle exec jekyll build --verbose