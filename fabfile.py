"""
You can see all commands with `$ fab -l`. Typical usages:
"""
from os import path, chdir

from fabric.api import run, local, cd, put, env
# from fabric.operations import prompt, get

env.use_ssh_config = True
here = path.abspath(path.dirname(__file__))
chdir(here)

DIR_REMOTE = "/server/website"

# Default hosts
if not env.hosts:
    env.hosts = ["somehost"]


def clean():
    local("cd source && rm -rf _site .jekyll-metadata .sass-cache/")


def upload():
    """ Upload website to server """
    print "Building current site..."
    clean()
    local("cd source && JEKYLL_ENV=production jekyll build --lsi")
    print
    print "This will update the webserver with the current version of the website."
    print
    print "Press enter to continue."
    raw_input()

    local("cd source/_site && tar -czf /tmp/blog.tar.gz *")
    put("/tmp/blog.tar.gz", "%s/" % DIR_REMOTE)
    with cd(DIR_REMOTE):
        run("tar -xf blog.tar.gz")
        run("rm -f blog.tar.gz")
    run("chown ubuntu %s -R" % DIR_REMOTE)
    clean()
    print "Website updated!"

#
# def ping_searchengines():
#     local("curl -s http://www.google.com/webmasters/sitemaps/ping?sitemap=https://www.metachris.com/sitemap.xml -o /dev/null")
#     local("curl -s http://www.bing.com/webmaster/ping.aspx?siteMap=https://www.metachris.com/sitemap.xml -o /dev/null")
#

def serve():
    """ Run `jekyll serve --watch` """
    # local("cd source && jekyll serve --config _config.yml,_config-dev.yml --watch --incremental")
    local("cd source && jekyll serve --config _config.yml,_config-dev.yml --watch --incremental")
