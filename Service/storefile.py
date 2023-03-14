from Config import databaseconnectionfile
from Mapper import prepareobjectfile

def mcqstore(email,mcqDict):
    Objfirebase = databaseconnectionfile.databaseconnection()
    
    mcqdetail = prepareobjectfile.preparemcq(email,mcqDict)
    
    try:
        Objfirebase.post('Account/EXAM/MCQ',mcqdetail)
        return True
    
    except:
        return False
    
    
