'''from Config import connectionfile

def createaccount(userid,password):
    status,value = connectionfile.connection()
    
    if (status):
        try:
            authobj = value.auth()
            print(authobj)
            authobj.create_user_with_email_and_password(userid,password)
            print("account created")
            
            return True
        
        except:
            print("account not created")
        
            return False
    
    else:
        print("inside else")
        return False
'''
from Config import connectionfile
from firebase import firebase

def createaccount(email_id,password):
    #call the connect the server
    status,value=connectionfile.connection()
    if status:
        print("connection is started")
        try:
            auth_obj=value.auth()
            auth_obj.create_user_with_email_and_password(email_id, password)
            print("account created")
            
            return True
        except:
            
            print("account already created")
            return False
    else:
        print("connection is not done") 
        
createaccount('nidhishnidhi45@gmail.com','nidhish@#28')
        