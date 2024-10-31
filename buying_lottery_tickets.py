#Replace MyUsername with your real username (Don't remove quotation marks!)
username = "MyUsername"

#Replace secretPassword with your real password (It is used to login to hexrpg.com) (Don't remove quotation marks!)
password = "secretPassword"

# Replace that 2 with how many tickets you want to buy.
how_many = 2

#This is link to lottery ticket. You can change it to mass buy something else :)
link_to_item = "https://www.hexrpg.com/store/store.php?store_id=1&item_id=233"


#Real code is here
import requests
import time
import random

payload = {'username': username, 'password': password, 'remember': 'yes', 'screenwidth': '1920', 'screenheight': '1080', 'action': 'submit'}

buy = {'buy': '1', 'g': '500', 's': '0', 'k': '0', 'submit': '   Pay   '}


with requests.Session() as s:
    login = s.post('https://www.hexrpg.com/login.php', data=payload)
    for l in range(how_many):
        s.post(link_to_item, data=buy)
        print("Buying " + str(l+1) + " item.")
        time1 = random.randint(1, 2) + random.random()
        time.sleep(time1)
        
    
    print("Done.")
            
        