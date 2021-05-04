# Importing Libs
from src.Audio2Text import Audio2Text
# Global text
text = 'We have listened a lot Now: '


# Driver Function
if __name__ == '__main__':
    # listen via Microphone
    a2t = Audio2Text()
    text = a2t._listen()
    # output
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
    print("Final Text Collected is: ", text)
    print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
    print("App Closed.")
