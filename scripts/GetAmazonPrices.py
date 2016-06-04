#! /usr/bin/env python3

import bs4, requests, pyperclip, fake_useragent

def getAmazonPrice(productUrl):
    user_agent = {'User-Agent': fake_useragent.UserAgent().random}
    
    res = requests.get(productUrl, headers = user_agent)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    price = soup.select('#priceblock_ourprice')
    title = soup.select('#productTitle')

    return str('The price for ' + title[0].text.strip() + ' is ' + price[0].text.strip())

amazonLink = pyperclip.paste()

if 'amazon' not in amazonLink:
    raise NameError('Not Amazon Link')

print(getAmazonPrice(amazonLink))
