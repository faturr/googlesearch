import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from googlesearch import search
query = input("INPUT SEARCH: ")
for i in search(query, tld="com", num=50, stop=310, pause=10, tbs="qdr:d"):
    print(i)
    
    