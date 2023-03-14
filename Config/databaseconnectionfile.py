from firebase import firebase

def databaseconnection():
    
    try:
        objfirebase = firebase.FirebaseApplication("https://firstapplication-e50c5-default-rtdb.firebaseio.com")
        return objfirebase
    
    except:

        return "null"