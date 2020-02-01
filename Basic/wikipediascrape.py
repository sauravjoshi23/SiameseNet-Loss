import requests
import pandas as pd
from bs4 import BeautifulSoup
Link = "https://en.wikipedia.org/wiki/"
Link_text = requests.get(Link).text
soup = BeautifulSoup(Link_text,'lxml')
#print(soup.prettify())#printing the whole data
our_table = soup.find('table')
#print(our_table)#searching for a particular table 
table_links = our_table.find_all('a')
#print(table_links)
billionares = []
for links in table_links:
    billionares.append(links.get('title'))
#print(billionares)

df = pd.DataFrame(billionares)
print(df)
