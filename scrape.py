# Import required libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# Create the request object  with the link tot he target site and header
# to send additional data with the url of target site, we need to use Request Object.
req = Request('http://webscraper.io/test-sites/e-commerce/static', headers={'User-Agent': 'Mozilla/5.0'})


# Lets get the content of the site using urlopen
# This returns an HTTPResponse object
page = urlopen(req)

# pass this to BeautifulSoup and get the HTML structure of the page.
# Here the 2nd argument html.parse specifies the type.
soup = BeautifulSoup(page, 'html.parser')

# In the result of parsing, search for all the elements with class 'title'
# soup.find_all return all the elements, alternatively if we want only one element we can use find. attrs specifies the attribute with which we want to search the html. Here I am using class.
items = soup.find_all('a', attrs={'class': 'title'})


# Open the file called test
f = open('test','a+')

# Loop over this and get the value to get the names of the items
for title in items:
	title_data = title.get("title")
	print(title_data)
	f.write(title_data+"\n")

f.close()

