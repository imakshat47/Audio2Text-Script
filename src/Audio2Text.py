try:
    import speech_recognition as sr
except:
    exit("speech_recognition Not Found.")
import threading
import app
from time import sleep
from src.Module import API, SentimentScore, Database


class Audio2Text(object):
    def __init__(self):
        print("System Up...")
        sleep(app.app_sleep_time)
        print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
        print("Available Devices => ", sr.Microphone.list_microphone_names())
        print("//-/-/-/-/-/-/-/-/-/-/-/-/-//")
        sleep(app.app_sleep_time)
        self.__r = sr.Recognizer()
        self.__text = ' '   
        self.__polarity = 0     
        self._sleep_time = 0.5

    def __audio2text(self, audio):        
        print("Listening...")     
        sleep(app.app_sleep_time)
        try:
            print("Got it! Now to recognize it...")
            sleep(self._sleep_time)  # sleep for a little bit         
            _text = self.__r.recognize_google(audio)
            sleep(self._sleep_time)  # sleep for a little bit   
            # IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
            # IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
            # _text = self.__r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
            # print("Text: ", _text)
            self.__text += " " + _text
            txt_sentiment = SentimentScore(self.__text)                                    
            _polarity = txt_sentiment._score("Intermediate Text")
            self.__polarity = (self.__polarity  + _polarity) / 2 
            # print("Score: ", self.__polarity)
            txt_sentiment._ordinals(self.__polarity)
        except sr.UnknownValueError:
            print("Oops! Didn't catch that...")
        except:
            print("Uh oh! Couldn't request results ", app._slow_internet_err)   
        print("System Running...")
        return None

    def _listen(self):
        try:
            threads = []
            m = sr.Microphone()
            print(app.silence_msg)
            with m as source:
                self.__r.adjust_for_ambient_noise(source)
            print(app.say_something_msg)
            while True:
                # Listen Microphone
                with m as source:
                    audio = self.__r.record(
                        source, duration=app.listening_duration)
                # audio = self.__r.listen(source)

                # makes threads
                thread = threading.Thread(
                    None, target=self.__audio2text, args=(audio,), daemon=True)
                threads.append(thread)                
                thread.start()

        except KeyboardInterrupt:
            pass

        # // Present Output
        # Cleaning Threads
        print(app.clean_thread_msg)                    
        while  len(threads) != 0:
            for thread in threads:
                # print("Thread: ", thread)
                # print(app.active_thread_left_msg, threading.active_count())
                thread.join()
                print("Cleaning...")
                threads.pop(0)
                # print(len(threads))
                # print(threads)
                sleep(self._sleep_time)  # sleep for a little bit   
        # print(app.active_thread_left_msg, threading.active_count())
        sleep(app.app_sleep_time)
        if len(threads) == 0:
            sleep(app.app_sleep_time)
            print("Threads Cleaned.")
        sleep(self._sleep_time)  # sleep for a little bit   
        # Min length
        if len(self.__text) <= app.min_text_len:
            print(app.min_text_len_msg, app.min_text_len)
        sleep(self._sleep_time)  # sleep for a little bit   
        # Processing
        print(app.final_text_msg, self.__text)        
        txt_sentiment = SentimentScore(self.__text)
        _polarity = txt_sentiment._score("Text")
        sleep(app.app_sleep_time)
        # ATS
        api = API()
        sleep(app.app_sleep_time)
        _text = api._mts(self.__text)        
        # Translated                
        print(app.mst_text, _text)
        txt_sentiment = SentimentScore(_text)
        _mts_polarity = txt_sentiment._score("Translated Text")
        
        sleep(app.app_sleep_time)
        ats_text = api._ats(_text)
        # ATS
        print(app.ats_text, ats_text)
        ats_txt_sentiment = SentimentScore(ats_text)
        _ats_polarity = ats_txt_sentiment._score("ATS Text")

        sleep(app.app_sleep_time)
        # Database
        to_push = input(app.db_push_msg)
        if to_push == "No" or to_push == "no":
            print("No data pushed to Database!!")
        else:
            _obj = {"_text": self.__text, "_ats_text": ats_text, "_mts_text": _text,
                    "_polarity": _polarity, "_ats_polarity": _ats_polarity,"_mts_polarity": _mts_polarity, "avg_polarity": self.__polarity}
            print(_obj)
            db = Database()
            sleep(app.app_sleep_time)
            db._insert(_obj)
        sleep(self._sleep_time)  # sleep for a little bit 
        txt_sentiment._ordinals(_polarity)
        sleep(self._sleep_time)  # sleep for a little bit 
        # Active thread left
        print(app.active_thread_left_msg, threading.active_count())
        print(threading.current_thread())
