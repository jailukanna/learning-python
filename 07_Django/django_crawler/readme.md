# Optional Assignment: Django Crawler

+ You'll be creating a web crawler using a pip module called 'BeautifulSoup'. Your web crawler will be able to access any website and retrieve the content of that page. You will then display information you find in a template.

+ This can be useful if you'd like to retrieve data from websites that are updated frequently and may not have an API designed to serve you that data.

First, install this pip module in your virtual environment:

`pip install beautifulsoup4`

+ Now, we'll practice retrieving some information from the Coding Dojo website. Try making a new document and running the following code. What do your results show?

	`
	from bs4 import BeautifulSoup
	from urllib2 import urlopen
	# set a url, first try Coding Dojo, then try pulling from a few of your favorite sites!
	url = 'http://www.codingdojo.com'
	# ask beutiful soup to open the below url and parse all html
	soup = BeautifulSoup(urlopen(url), "html.parser")
	# and print the results!
	print soup
	`

+ Simple! In just 3 lines of code you were able to retrieve all the HTML code from Coding Dojo's landing page! What else can you retrieve? Here's some code that will allow you to grab each link from Coding Dojo's website. Add this to the above code.

	`
	# add at the top of the document with your other import
	from urllib2 import urlopen
	# helper function makes a list of all 'a' tag contents with a key of ''
	def makeUrlList():
    		urlArr = []
    		for i in range(len(soup('a'))):
        		urlArr.append(soup('a')[i]['href'])
    		return urlArr
		list = makeUrlList()
		print list
	def makeUrlDictionary():
    		urlDict = {}
    		for i in range(len(soup('a'))):
        		if urlDict.has_key(soup('a')[i]['href']):
            			urlDict[soup('a')[i]['href']] += 1
        		else:
            			urlDict[soup('a')[i]['href']] = 1
    		return urlDict
		print makeUrlDictionary()
		`

+ Run the code and check out what is printed to your console. Spend some time understanding what this code does. You will find the documentation helpful here.

+ Now find several websites from which you'd like to scrape some data. Set up at least 3 routes to serve up data from different websites. Incorporate the scraped data into your templates. Have at least 3 templates with data from 3 different websites.
