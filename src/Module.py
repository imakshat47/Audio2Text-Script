try:
    import requests
    import json
    from bs4 import BeautifulSoup
    import app
    from textblob import TextBlob
except:
    exit("Some Modules Missing!!")
try:
    import key
except:
    exit("key Not Found.")

try:
    from pymongo import MongoClient
except:
    exit("pymongo Not Found.")


class API(object):
    def __init__(self):
        print("Trying to connect APIs...")

    def _ats(self, ats_text, _number_of_lines=4, _algoritm_number=1):
        # params Json
        _params = {'csrfmiddlewaretoken': app._csrf_token, 'url': '',
                   'long-text': ats_text, 'number': _number_of_lines, 'algorithm': _algoritm_number}
        # request
        try:
            r = requests.get('http://automatictextsummarizer.herokuapp.com/summarize_page',
                             params=_params, headers={'accept': 'application/json'})
            if r.status_code == 200:
                print("Connection success...")
                soup = BeautifulSoup(r.text, 'html.parser')
                get_tags = soup.findAll('p')
                # ATS Text
                ats_text = get_tags[1].text
            else:
                print("Connection failed...")
        except:
            print(app._slow_internet_err)
        return ats_text


class SentimentScore(object):
    def __init__(self, text):
        self.__senti = TextBlob(text).sentiment

    def _score(self, _of):
        print(_of, app.sentiment_score_msg, self.__senti.polarity)
        print(_of, app.subjectivity_score_msg, self.__senti.subjectivity)
        return self.__senti.polarity


class Database(object):
    def __init__(self):
        try:
            self.__client = MongoClient(key._mongo_uri)
            __coll = self.__client[key._db_name]
            self.__db = __coll[key._db_document]
            print(app.db_conn_succ_msg)
        except:
            print(app.db_conn_err_msg)

    def _insert(self, _obj):
        self.__db.insert_one(_obj)
        print(app.saved_to_db_msg)

    def __del__(self):
        self.__client.close
        print(app.db_closed)
