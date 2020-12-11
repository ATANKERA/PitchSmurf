import requests
from bs4 import BeautifulSoup


companyname = "alphabet"

tickerurl = 'https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup=' + companyname + '&Country=us&Type=All'
content = requests.get(tickerurl)
soup = BeautifulSoup(content.text, 'html.parser')
section = soup.find_all('tr')[1]
target = soup.find_all('td')[0].get_text()

print(target)
