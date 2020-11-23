import os
import amino
os.system ('clear')
os.system ('pkg install python')
os.system ('pip install Amino.py')
os.system ('clear')
e =input ('Enter your Email:')
p = input ('Enter your Password:')
clint=amino.Client()
clint.login(email=e,password=p)
listblockers=clint.get_blocker_users(start=0,size=100)
for id in listblockers:
    print('ndc://g/user-profile/'+id)