from Config import connectionfile

def insertmedia(imageData):
    try:
        status, firebase = connectionfile.connection()
        
        storageObject = firebase.storage()
    
        storageObject.child(imageData).put(imageData)
    
        #print("Sent Media")
        
        return True
    
    except:
        #print("Not Sent Media")
        return False
        