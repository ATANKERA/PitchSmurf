import requests
from bs4 import BeautifulSoup

def ticker(thecompanynane):

    companyname = ""
    companyname = thecompanynane
    if companyname == "":
        companyname = "alphabet"

    tickerurl = 'https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup=' + companyname + '&Country=us&Type=All'
    content = requests.get(tickerurl)
    soup = BeautifulSoup(content.text, 'html.parser')
    section = soup.find_all('tr')[1]
    target = soup.find_all('td')[0].get_text()

    return target


def overview(symbol):

    #overview
    yahoourl = 'https://finance.yahoo.com/quote/' + symbol + '/profile?p=' + symbol
    content = requests.get(yahoourl)

    soup = BeautifulSoup(content.text, 'html.parser')
    section = soup.find_all('span')
    store = [x.get_text() for x in section]

    sector = store[43]

    section = soup.find_all('p')
    store = [x.get_text() for x in section]
    description = store[2]


    #key shareholders
    yahoourl = 'https://finance.yahoo.com/quote/' + symbol + '/holders?p=' + symbol
    content = requests.get(yahoourl)

    soup = BeautifulSoup(content.text, 'html.parser')
    section = soup.find_all('td')
    store = [x.get_text() for x in section]

    invest1 = store[8]
    invest2 = store[13]


    #financials
    yahoourl = 'https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol
    content = requests.get(yahoourl)

    soup = BeautifulSoup(content.text, 'html.parser')
    section = soup.find_all('span')
    store = [x.get_text() for x in section]

    mktcap = store[68]
    peratio = store[72]
    eps = store[74]

    #valuation
    soup = BeautifulSoup(content.text, 'html.parser')
    section = soup.find_all('div')
    store = [x.get_text() for x in section]

    rating = store[187]
    estreturn = store[188]

    return "" +sector +" --- "+ description +" --- "+ invest1 +" --- "+ invest2 +" --- "+ mktcap +" --- "+ peratio +" --- "+ eps +" --- "+ rating +" --- "+ estreturn



# print(overview("AAPL"))
