from firebase import firebase
import pyrebase

def connection():
    try:
        firebaseConfig = {
              'apiKey': "AIzaSyAM90zCSMSZWBhGQ33kjZW8nobyB1vh44c",
              'authDomain': "firstapplication-e50c5.firebaseapp.com",
              'databaseURL': "https://firstapplication-e50c5-default-rtdb.firebaseio.com",
              'projectId': "firstapplication-e50c5",
              'storageBucket': "firstapplication-e50c5.appspot.com",
              'messagingSenderId': "364042201861",
              'appId': "1:364042201861:web:e6eafda39920108c5d256c",
              'measurementId': "G-TW85XWCVGQ"
        }
        
        firebase = pyrebase.initialize_app(firebaseConfig)
        
        return True,firebase
    
    except:
    
        return False,"null"