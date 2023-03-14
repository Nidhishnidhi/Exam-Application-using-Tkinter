from Config import databaseconnectionfile

def insertdetail(dataDict):
    objfirebase = databaseconnectionfile.databaseconnection()
    
    try:
        objfirebase.post('Account/PersonalData',dataDict)
        
        return True
    
    except:
        
        return False