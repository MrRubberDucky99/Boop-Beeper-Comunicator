import numpy as np, json, time, struct, datetime, Message

def dataMode(mode):
    dataOut=format(65, '7b') #Everyone In range Message
    if mode == 0:
        dataOut=format(66, '7b') #Ping, non hashed
    elif mode == 1:
        dataOut=format(67, '7b') #Ping, hashed
    elif mode == 2:
        dataOut=format(68, '7b') #Message, non hashed
    elif mode == 3:
        dataOut=format(69, '7b') #Message, hashed
    elif mode == 4:
        dataOut=format(70, '7b') #Message Received, non hashed
    elif mode == 5:
        dataOut=format(71, '7b') #Message Received, 
    return str(dataOut).replace(" ", "0")

def UTCBin():
    now = datetime.datetime.now() #Gets The Time
    stamp = time.mktime(now.timetuple())
    binarydatetime = struct.pack('<L', int(stamp))
    recoverbinstamp = struct.unpack('<L', binarydatetime)[0]
    return str(format(recoverbinstamp, '64b')).replace(" ", "0") #Outputs time as binary

def getID():
    settings = open("Settings.json", 'r')#Opens JSON file
    settingsJSON = json.load(settings) #Imports JSON data
    ID = settingsJSON["ID"][0]["IDbin"] #Looks for ID
    settings.close()#Closes JSON
    return ID 

def getAllContacts():
    contacts = open("Code/Contacts.json", 'r') #Opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    contacts.close() #Closes JSON
    return contactsJSON["Contacts"] #Returns all Contacts

def getContacts():
    contacts = open("Code/Contacts.json", 'r') #Opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    x=0
    for i in contactsJSON["Contacts"]:
        x=x+1
        i=i
    contacts.close() #Closes JSON
    return x #Returns all Contacts

def getContact(Name, IDType):
    contacts = open("Code/Contacts.json", 'r') #opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    x=0
    for i in contactsJSON["Contacts"]:
        if contactsJSON["Contacts"][x]["Name"] == Name: #Looks For Name entered in json file
            x=x
            break
        else:
            x=x+1
        i=i
    if IDType == "ascii": contactID = contactsJSON["Contacts"][x]["IDascii"] #Returns Ascii ID
    elif IDType == "bin": contactID = contactsJSON["Contacts"][x]["IDbin"] #Returns Binary ID
    else: contactID = contactsJSON["Contacts"][x]["IDascii"] #Returns Ascii ID
    contacts.close() #Closes JSON File
    return contactID #Returns Contact ID.

def getContactInfo(Num):
    contacts = open("Code/Contacts.json", 'r') #opens JSON
    contactsJSON = json.load(contacts) #Imports JSON
    contact = [contactsJSON["Contacts"][Num]["Name"], contactsJSON["Contacts"][Num]["IDascii"]]
    contacts.close() #Closes JSON File
    return contact #Returns Contact ID.

def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        ##uptime_string = str(datetime.timedelta(seconds = uptime_seconds))
    return uptime_seconds

print(getContactInfo(0)[0])