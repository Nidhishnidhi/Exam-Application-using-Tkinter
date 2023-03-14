from Config import connectionfile

def logintoaccount(email,password):
    status,value = connectionfile.connection()
    
    if(status):
        try:
            authObj = value.auth()
            authObj.sign_in_with_email_and_password(email,password)
            
            return True
            
        except:
            return False
        
    else:
        return False