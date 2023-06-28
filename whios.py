import whois # pip install python-whois
import enchant 
d = enchant.Dict("en_US")

import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
    



def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
num='abcdefghijklmnopqrstuvwxyz'
stoppedname='antetypes'
num1=[*num]
file2=open('new2.txt','a')
file3=open('words_alpha.txt','r')
for i in file3.readlines():

    if bool(connect())==True:
    
        if len(i)>4 and len(i)<13:
            if bool(is_registered(i.strip('\n')+'.com'))==False:
                
                file2.write(i)
                file2.flush()
                
                
                print(i,'is not registered')
            else:
                print(i)
    else:
        break
    
    
file2.close()


# domain=[]
# d.check('')
# j='.org'
# file = open('text.txt','r')
# for i in file.readlines():
#     if bool(is_registered(i.strip('\n')+j))==False:
#         print(i,'not registered')
#     else:
#         print(i,'is registered')
# i=''
# # print(is_registered(i+'.com'))
# if bool(is_registered(i+'.com'))==True:
#         print(i,'is registered')
# else:
#      print(i,'not registered')



