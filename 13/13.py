# http://www.pythonchallenge.com/pc/return/disproportional.html


import xmlrpc.client

def Phonebook(name):
    XMLRPC_SERVER_URL = "http://www.pythonchallenge.com/pc/phonebook.php"

    proxy = xmlrpc.client.ServerProxy( XMLRPC_SERVER_URL )
    # print(proxy)
    # print(proxy.system.listMethods())
    # print(proxy.system.methodHelp('phone'))
    print(proxy.phone(name)) # "Bert is evil was stated in challange 12, evil4.gpx

# 555-ITALY


Phonebook('Bert')