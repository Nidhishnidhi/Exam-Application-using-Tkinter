from Config import connectionfile


def retrievedata(email):
    status, value = connectionfile.connection()
    
    databaseobj = value.database()
    data = databaseobj.child('Account/PersonalData').get()
    
    for each_data in data:
        sample_email = each_data.val()['email']
        if(sample_email == email):
            data = each_data.val()
            break
        
    return True,data

def retrievetime(email):
    time = "not recorded"
    try:
        status,value = connectionfile.connection()
        
        timeobj = value.database()
        time = timeobj.child("Account/Logintime").get()
        
        for each_time in time:
            sample_email = each_time.val()['email']
            if(sample_email == email):
                time = each_time.val()
                return True,time
    except:
        return False,time
   