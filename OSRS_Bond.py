import requests 
import re
from bs4 import BeautifulSoup

URL = 'http://services.runescape.com/m=itemdb_oldschool/Old+school+bond/viewitem?obj=13190'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='grandexchange')
job_elems = results.find('div', class_='stats')
price = job_elems.find('h3')
price2  = price.find('span')
final = str(price2)
final = re.findall(r'"(.*?)"', final)
elem = final[0]
elem = elem.replace(',', "")
price = int(elem)
print(price)
#End web scrapping for Item
#Start comparison
buyPrice = 4500000  #Fill here
breakEvenPoint = buyPrice * 1.1 #because 10% tax, essentially this is the buy price because you have to make it tradable
profitGoal =  2.5 #FILL HERE for bonds it fluctuates between +/- 5% so ill do 2.5
notifyPrice = breakEvenPoint * (1 + (profitGoal/100))
print(notifyPrice)



