# Real Time Opinoin Mining System

## Functions:

1. Listen Microphone
2. Preform Opinion Mining
3. Return Result to user
4. Push result to database

## How to run

1. Clone my Repo
2. Connect Microphone
3. Open CMD
4. Make a key.py file in root dir for connecting database (If want to push Record to Database)

- File format

```python
   _mongo_uri = "URI"
   _db_name = "tenet"
   _db_document = "audioText"
```

5. Activate a virtual env
```python
 pip install virtualenv
 virtualenv env
 env\Scripts\activate
```

6. Run

```python
 pip install pipwin
 pipwin install pyaudio
```

Note: Error While running pyaudio:
   1. For Python 3.9.x: pip install asset/PyAudio-0.2.11-cp39-cp39-win_amd64.whl
   2. For Python 3.7.x: pip install asset/PyAudio-0.2.11-cp37-cp37-win_amd64.whl


7. Run

```python
 pip install -r requirements.txt
```

8. Run 
```pyhton
   py main.py
```


9. Play the Audio and Everything will be done by script.


10. Press Ctrl + c to stop the script and push data to DB.

