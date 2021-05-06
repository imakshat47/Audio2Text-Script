# Importing Libs
from src.Audio2Text import Audio2Text

# Driver Function
if __name__ == '__main__':
    # listen via Microphone
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
    print("                               Welcome to Tenet System")
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
    a2t = Audio2Text()
    a2t._listen()    
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
    print("App Closed.")
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")