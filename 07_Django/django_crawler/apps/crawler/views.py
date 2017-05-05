from django.shortcuts import render
from bs4 import BeautifulSoup # import `beautifulsoup4` for building web crawler
from urllib2 import urlopen # allows us to feed a URL to beautifulsoup4

def index(request):
    """Loads index page and crawls any pages defined."""

    print "Running index method..."
    print "Testing crawl methods..."

    #-------------------------#
    #-- TESTING OUR METHODS --#
    #-------------------------#
    # Will crawl our given URL and spit out `pretty` HTML (formatted with appropriate tabs and spacing).
    print "##### BEGIN PRETTY HTML #####"
    print(__crawl("http://www.codingdojo.com").prettify())
    print "###### END PRETTY HTML ######"

    # Print URL list from crawled data using methods within `__crawl()`:
    print "####### BEGIN URL LIST #######"
    print(make_url_list(__crawl("http://www.codingdojo.com")))
    print "######## END URL LIST ########"

    # print URL dictionary with occurrences count of each link:
    print "####### BEGIN URL DICTIONARY #######"
    print(make_url_dict(__crawl("http://www.codingdojo.com")))
    print "####### END URL DICTIONARY #######"
    #-------------------------#
    #-- END METHODS TESTING --#
    #-------------------------#

    # Save URL dictionary for Template usage:
    urls = {
        "data" : make_url_dict(__crawl("http://www.google.com"))
    }

    # Load index.html page and send URL dictionary to Template:
    return render(request, "crawler/index.html", urls)

def __crawl(web_address):
    """Crawls URL provided and returns HTML.

    Parameters:
        - web_address: the URL to crawl.
    """

    print "Crawling: {} ....".format(web_address)

    # Use `BeautifulSoup` to parse all HTML for our given web address:
    soup = BeautifulSoup(urlopen(web_address), "html.parser")

    # Returns `soup` object:
    return soup

def make_url_list(soup_data):
    """Make list of href URL strings inside all anchor tages."""

    # Create an empty list which will hold `href` tags:
    url_list = []

    print "Extracting `href` tags from anchors from crawled website data..."

    # Loop through `soup_data` object in the range of 0 to the number of `<a>` objects inside of `soup_data`:
    for i in range(len(soup_data('a'))):
        # Add *each* `href` string (thus the `i`) of each `<a>` to the list:
        url_list.append(soup_data('a')[i]['href'])

    print "Extraction complete. {} total URLs extracted...".format(len(url_list))

    # Return the URLs list:
    return url_list

def make_url_dict(soup_data):
    """Makes dictionary object of each URL along with a count of how often it occurs in the HTML document."""

    # Create empty dictionary file which will hold URLs and a count for how often each occur:
    url_dict = {}

    print "Extracting `href` tags and counting occurrences from crawled website data..."

    # Loop through each `<a>` tag inside of `soup_data` object:
    for i in range(len(soup_data('a'))):
        # If the URL already exists in our dictionary, increase its count:
        if url_dict.has_key(soup_data('a')[i]['href']):
            # Increase the value (which is a count) by `1`:
            url_dict[soup_data('a')[i]['href']] += 1
        # Otherwise, set the URL to the dictionary key and set the count to `1`:
        else:
            url_dict[soup_data('a')[i]['href']] = 1

    print "Extraction complete."
    # Return the new URL dictionary:
    return url_dict
