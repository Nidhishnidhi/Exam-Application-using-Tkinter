from Config import connectionfile

def retrievemcqdata(email):
    status, value = connectionfile.connection()
    flag = 0
    empty = []
    databaseobj = value.database()
    data = databaseobj.child('Account/EXAM/MCQ').get()
    
    for each_data in data:
        sample_email = each_data.val()['Email']
        if(sample_email == email):
            data = each_data.val()
            flag = 1
            break
    if flag == 1:
        d = data['McqQuestionAnswer']
    
        return True,d
    
    else:
        return False,empty



def retrievesbqdata(email):
    try:
        status, value = connectionfile.connection()
        '''flag = 0
        #empty = 0
        percentage = 0
        alldata = []'''
        databaseobj = value.database()
        data = databaseobj.child('Account/EXAM/SBQ').get()
        
        for each_data in data:
            sample_email = each_data.val()[0]
            if(sample_email == email):
                originaldata = each_data.val()
                flag = 1
                break
        '''if flag == 1:
            for i in range(5):
            
                for each_data in data:
                    newemail = each_data.val()[0]
                    print(newemail)
                    if(newemail != email):
                        question = each_data.val()[i+1]
                        print(question)
                        
                        if(question == originaldata[i+1]):
                            percentage += 100
                            print(percentage)
                            break
                            
                    
            percentage = percentage // 5
            print("final",percentage)
    
            return True,percentage
    
        else:
            return False,'Null' '''
        print(originaldata)
        
        return True,originaldata[6]
    
    except:
        return False,originaldata[6]
    
    
def beforeuploading(email,answers):
    flag = 0
    #empty = 0
    percentage = 0
    alldata = []
    try:
    
        status, value = connectionfile.connection()
        
        databaseobj = value.database()
        data = databaseobj.child('Account/EXAM/SBQ').get()
        
        for i in range(5):
        
            for each_data in data:
                question = each_data.val()[i+1]
                print(question)
                
                if(question == answers[i]):
                    percentage += 100
                    print(percentage)
                    break
                        
                
        percentage = percentage // 5
        print("final",percentage)
    
        return True,percentage
    
    except:
        return False,percentage
    

    
    

