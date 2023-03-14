from Config import databaseconnectionfile
from Mapper import prepareobjectfile
from datetime import datetime

def logintimestore(email):
    Objfirebase = databaseconnectionfile.databaseconnection()
    
    currenttime = datetime.now()
    datetimedetails = currenttime.strftime("%d/%m/%Y %H:%M:%S")
    
    logindetail = prepareobjectfile.prepareobjectlogintime(email,datetimedetails)
    
    try:
        Objfirebase.post('Account/Logintime',logindetail)
        return True
    
    except:
        return False