try:
    import speech_recognition as sr
except:
    exit("speech_recognition Not Found.")
try:
    from pymongo import MongoClient
except:
    exit("pymongo Not Found.")
try:
    import key
except:
    exit("key Not Found.")
import threading
from time import sleep


class Audio2Text(object):
    def __init__(self):
        print("Devices => ", sr.Microphone.list_microphone_names())
        print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
        self.__r = sr.Recognizer()
        self.__text = ' '
        __client = MongoClient(key._mongo_uri)
        __coll = __client[key._db_name]
        self.__db = __coll[key._db_document]

    def __audio2text(self, audio):
        try:
            print("Listening...")
            sleep(5)
            # lannguage tag n  show_all=True
            _text = self.__r.recognize_google(audio)
            # _text = self.__r.recognize_google_cloud(audio)
            print("Text => ", _text)
            self.__text += " "
            self.__text += _text
        except Exception as e:
            print(e)
            print("Something went Wrong. But Still Listening...")
        return None

    def __add2db(self, _obj):
        self.__db.insert_one(_obj)

    def _listen(self):
        try:
            threads = []
            print("Started Listening...")
            while True:
                # Listen Microphone
                with sr.Microphone() as source:
                    # 2 * 60s = 120 // 2 mins
                    audio = self.__r.record(source, duration=120)

                thread = threading.Thread(
                    None, target=self.__audio2text, args=(audio,))
                thread.start()
                threads.append(thread)

        except KeyboardInterrupt:
            pass

        if len(self.__text) >= 125:
            print("Saving to db...")
            sleep(5)
            _obj = {"text": self.__text}
            self.__add2db(_obj)
        else:
            print("Can't Save to db. Text length less than 125.")
        print("Cleaning threads...")
        sleep(5)
        for thread in threads:
            print("Active Thread Left => ", threading.active_count())
            thread.join()
        sleep(5)
        print(threading.current_thread())
        return self.__text
