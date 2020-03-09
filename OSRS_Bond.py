# pyinstaller --onefile -i [icon_file] [script name], reminder on how to convert .py to .exe
import requests 
import win10toast
import re
from bs4 import BeautifulSoup
import time


def bond(PB,goal,minimumPrice):
    while(1):
        toaster = win10toast.ToastNotifier()
        #http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=554 <--- can just change the object ID and it will iterate through the items :POGCHAMP: so just have a database that scrapes the name and price 
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
        minimumPriceToBuy = int(minimumPrice) #FILL HERE , minimum price you want to buy the item for 
        breakEvenPoint = buyPrice * 1.1 #because 10% tax, essentially this is the buy price because you have to make it tradable
        notifyPrice = breakEvenPoint * (1 + (profitGoal/100))

        if(price <= minimumPriceToBuy):
            toaster.show_toast('OSRS_BOND', 'Item has reached the price you are willing to buy for. BUY NOW', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\camera_test.ico")
       
        if (price >= notifyPrice): 
            toaster.show_toast('OSRS_BOND', 'Profit Margin Reached, SELL NOW', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\coin.ico")
            exit(0)
        else: 
            toaster.show_toast('OSRS_BOND', 'Profit Margin Not Reached', duration= 3,
            icon_path="D:\\Users\\sheeh\Desktop\\Projects\\OSRS Tools\\OSRS_Bond\\coin.ico")
            time.sleep(3600) #check every hour 


#------------- START GUI 
from tkinter import *
root = Tk()

title = Label(root, text="Notify OSRS") 
item = Label(root, text="Item: ") #should be drop down or search for items
priceBought = Label(root, text="What price did you buy the item for?")
goal = Label(root, text="What is your profit goal for this item?")
mPriceLabel = Label(root, text="When would you like to buy this item?")

#minimumbuyitem
#minimumbuyprice = Label(root, text="What price did you buy the item for?")

title.grid(row=0,column=0)
item.grid(row=1,column=0)
priceBought.grid(row=2,column=0)
goal.grid(row=3,column=0)
mPriceLabel.grid(row=4,column=0)


entryPB = Entry(root,width=30,borderwidth=3)
#entryPB.insert(0,"noob")
entryGoal = Entry(root,width=30,borderwidth=3)
mPrice = Entry(root,width=30,borderwidth=3)
entryPB.grid(row=2,column=1)
entryGoal.grid(row=3,column=1)
mPrice.grid(row=4,column=1)


def bond_click(PB,goal):
    print(PB+goal)

runButton = Button(root, text="Run!",padx=50,fg="white",bg="brown",command=lambda: bond(entryPB.get(),entryGoal.get(),mPrice.get()))
runButton.grid(row=5,column=1)



root.mainloop()

#-------------- END GUI




