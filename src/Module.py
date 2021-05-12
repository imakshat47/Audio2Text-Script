try:
    import requests
except:
    exit("Requests Not Found.")
try:
    from bs4 import BeautifulSoup
except:
    exit("Beautiful Soup Not Found.")

from textblob import TextBlob
try:
    import key
    _key = True
except:
    _key = False
    print("key.py Not Found.")
try:
    from pymongo import MongoClient
except:
    exit("pymongo Not Found.")
import app
import json

class API(object):
    def __init__(self):
        print("Connecting API...")

    def _ats(self, ats_text, _number_of_lines=4, _algoritm_number=1):
        if len(ats_text) <= 10:
            return ats_text
        # params Json
        _params = {'csrfmiddlewaretoken': app._csrf_token, 'url': '','long-text': ats_text, 'number': _number_of_lines, 'algorithm': _algoritm_number}
        # request
        try:            
            r = requests.get(app.ats_uri, params=_params, headers={'accept': 'application/json'})
            if r.status_code == 200:
                print("ATS ", app.status_succ)
                soup = BeautifulSoup(r.text, 'html.parser')
                get_tags = soup.findAll('p')
                # ATS Text
                ats_text = get_tags[1].text            
            else:
                print("ATS ", app.status_err)
        except:
            print(app._slow_internet_err)
            print("ATS ", app.status_err)
        return ats_text

    def _mts(self, text, lang="en"):
        try:
            r = requests.get(app.mts_uri, params={"text": text, "lang": lang})
            res = json.loads(r.text)                        
            if res['code'] != 200:
               raise Exception("Translation Status Code " + res['code'])
            print("MTS ", app.status_succ)
            text = res['data']['text']          
        except:
            print("Translation ", app.status_err)
        return text

class SentimentScore(object):
    def __init__(self, text):
        self.__senti = TextBlob(text).sentiment
        print("Sentiment Score ", app.status_succ)

    def _score(self, _of):
        _polairty = self.__senti.polarity
        print(_of, app.sentiment_score_msg, _polairty)
        print(_of, app.subjectivity_score_msg, self.__senti.subjectivity)
        return _polairty


class Database(object):
    def __init__(self):
        if _key == False:
            print("Key.py Missing!!")
            print("Database Connection ", app.status_err)
        else:
            try:
                self.__client = MongoClient(key._mongo_uri)
                __coll = self.__client[key._db_name]
                self.__db = __coll[key._db_document]
                print("Database Connection ", app.status_succ)
            except:
                print("Database Connection ", app.status_err)

    def _insert(self, _obj):
        if _key == True:
            self.__db.insert_one(_obj)
            print("Data Insertion ", app.status_succ)
        else:
            print("Data Insertion ", app.status_err)

    def __del__(self):
        if _key == True:
            self.__client.close
            print("Database Connection Closing ", app.status_succ)
        else:
            print("Database Connection Closing ", app.status_err)   