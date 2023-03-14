from Config import connectionfile

def retrievedata(email):
    status, value = connectionfile.connection()
    
    databaseobj = value.database()
    data = databaseobj.child('Account/EXAM/SBQ').get()
    
    for each_data in data:
        sample_email = each_data.val()['Email']
        if(sample_email == email):
            data = each_data.val()
            break
        
    d = data['McqQuestionAnswer']
    print(d['total'])
    return True,d
