'''
dnaindia.com
'''
import re
from calibre.web.feeds.news import BasicNewsRecipe

class DNAIndia(BasicNewsRecipe):

    title       = 'DNA India'
    description = 'Mumbai news, India news, World news, breaking news'
    __author__  = 'Kovid Goyal'
    language    = _('English')
    encoding    = 'cp1252'

    feeds       = [
                   ('Top News', 'http://www.dnaindia.com/syndication/rss_topnews.xml'),
                   ('Popular News', 'http://www.dnaindia.com/syndication/rss_popular.xml'),
                   ('Recent Columns', 'http://www.dnaindia.com/syndication/rss_column.xml'),
                   ('Mumbai', 'http://www.dnaindia.com/syndication/rss,catid-1.xml'),
                   ('India', 'http://www.dnaindia.com/syndication/rss,catid-2.xml'),
                   ('World', 'http://www.dnaindia.com/syndication/rss,catid-9.xml'),
                   ('Money', 'http://www.dnaindia.com/syndication/rss,catid-4.xml'),
                   ('Sports', 'http://www.dnaindia.com/syndication/rss,catid-6.xml'),
                   ('After Hours', 'http://www.dnaindia.com/syndication/rss,catid-7.xml'),
                   ('Digital Life', 'http://www.dnaindia.com/syndication/rss,catid-1089741.xml'),
                   ]
    remove_tags = [{'id':'footer'}, {'class':['bottom', 'categoryHead']}]

    def print_version(self, url):
        match = re.search(r'newsid=(\d+)', url)
        if not match:
            return url
        return 'http://www.dnaindia.com/dnaprint.asp?newsid='+match.group(1)

    def postprocess_html(self, soup, first_fetch):
        for t in soup.findAll(['table', 'tr', 'td']):
            t.name = 'div'

        a = soup.find(href='http://www.3dsyndication.com/')
        if a is not None:
            a.parent.extract()
        return soup
