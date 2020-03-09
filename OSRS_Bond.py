# pyinstaller --onefile -i [icon_file] [script name], reminder on how to convert .py to .exe
import requests 
import win10toast
import re
from bs4 import BeautifulSoup
import time

def bond():
    while(1):
        toaster = win10toast.ToastNotifier()
        URL = 'http://services.runescape.com/m=itemdb_oldschool/Old+school+bond/viewitem?obj=13190'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='grandexchange')
        job_elems = results.find('div', class_='stats')
        price = job_elems.find('h3')
        price2  = price.find('span') #have to clean up the price scrapping situation going on
        final = str(price2)
        final = re.findall(r'"(.*?)"', final)
        elem = final[0]
        elem = elem.replace(',', "")
        price = int(elem)
        # End web scrapping for Item
        #Start comparison
        buyPrice = 4500000  #FILL HERE, amount you bought the item for 
        profitGoal =  2.5 #FILL HERE for bonds it fluctuates between +/- 5% so ill do 2.5
        minimumPriceToBuy = 4500000 #FILL HERE , minimum price you want to buy the item for 
        breakEvenPoint = buyPrice * 1.1 #because 10% tax, essentially this is the buy price because you have to make it tradable
        notifyPrice = breakEvenPoint * (1 + (profitGoal/100))

        if(price <= minimumPriceToBuy):
            toaster.show_toast('OSRS_BOND', 'Item has reached the price you are willing to buy for. BUY NOW', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\coin.ico")
       
        if (price >= notifyPrice): 
            toaster.show_toast('OSRS_BOND', 'Profit Margin Reached, SELL NOW', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\coin.ico")
            exit(0)
        else: 
            toaster.show_toast('OSRS_BOND', 'Profit Margin Not Reached', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\coin.ico")
            time.sleep(3600) #check every hour 
    
bond()






