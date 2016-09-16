Complete Jekyll Blog Setup.

See http://www.metachris.com for a live example.


# Setup

On Linux

    apt-get install ruby-dev
    gem install jekyll-paginate
    gem install classifier-reborn


On Mac

    gem install jekyll bundler
    gem install jekyll-paginate
    gem install classifier-reborn


## Building the blog

The main config file is `src/_config.yml`

    cd source
    jekyll serve --config _config.yml,_config-dev.yml --watch --incremental

As a shortcut, you can use the Fabric command `fab serve`.

# Fabric Commands

[Fabric](http://www.fabfile.org/) is a tool to automate
tasks. You can install it with `pip install fabric`.

    # Serve local development version of the Blog
    fab serve

    # Update server
    fab upload
