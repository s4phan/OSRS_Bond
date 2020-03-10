import requests 
import re
from bs4 import BeautifulSoup

#http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=554 <--- can just change the object ID and it will iterate through the items :POGCHAMP: so just have a database that scrapes the name and price 

for i in range(5324,5400,2):
    URL = 'http://services.runescape.com/m=itemdb_oldschool/viewitem?obj={}'.format(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='grandexchange')
    try:
        derp = results.find('div', class_="item-description")
        name = derp.find('h2')
        name = re.search('>(.*)<',str(name))
       #----------- Above is for item name 
       #--------- Below is for price
        job_elems = results.find('div', class_='stats')
        price = job_elems.find('h3')
        price2  = price.find('span') #have to clean up the price scrapping situation going on
        final = str(price2)
        final = re.findall(r'"(.*?)"', final)
        elem = final[0]
        elem = elem.replace(',', "")
        price = int(elem)
        
        print(name.group(1))
        print(price)
    except AttributeError:
        print('Failed to parse url')
        print(page.status_code)
    

  






