
# Web search via Google
def searchWeb(query):
# Import Google search library (and also beautifulsoup4)
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

# Display the results
    for i in search(query, tld="co.in", num=15, stop=10, pause=2):
        print(i)


searchWeb("A decent discord server")

# Source for reference: 
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/ 
