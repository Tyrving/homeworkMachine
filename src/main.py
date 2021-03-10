# Import Google search library (and also beautifulsoup4)
from googlesearch import search 
from bs4 import BeautifulSoup
import urllib.request
import random

# Web search via Google
def searchWeb(query):

# Display the results
    for i in search(query, tld="co.in", num=15, stop=10, pause=2):
        print(i)

# More specific web search
def searchWebSpecific(query, sourceFile):

# Two lists: One for sources, one for results from Google. There may be a better way to do this but I don't care ATM
    sources = []
    results = []
    filtered = []

# Chuck all sources into a list object for convinience
    with open(sourceFile) as fp:
        sources = fp.read().splitlines()

# As we're searching, check and see if any of the results match up with the url's in the string
    for i in search(query, tld="co.in", num=15, stop=20, pause=2.0):
        results.append(i)
    
    for i in results:
        for x in sources:
            if x in i:
                filtered.append(i)

    print(filtered)

# Source for reference: 
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/ 

# Some notes on the web search loop:
# query : query string that we want to search for.
# lang : lang stands for language
# numResults : Number of results we want.
# stopRes : Last result to retrieve. Use None to keep searching forever.
# pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.


# quickAnswer script is for exactly what it looks like: A quick answer to a question, without using Google.
def quickAnswer():
    url = 'https://google.com/search?q=What+is+the+answer+to+life+the+universe+and+everything'
    
    request = urllib.request.Request(url)

    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    html = raw_response.decode("utf-8")
    
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.select("#search div.g")
    for div in divs:
        results = div.select("h3")

        if (len(results) >= 1):

            h3 = results[0]

            print(h3.get_text())
