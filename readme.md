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
4. Make a key.py file in root dir for connecting database

- File format

```python
   _mongo_uri = "URI"
   _db_name = "tenet"
   _db_document = "audioText"
```

5. Run

```python
 pip install pipwin
 pipwin install pyaudio
```

5. Run

```python
 pip install -r requirements.txt
```

6. Run 
```pyhton
   py main.py
```
7. Play the Audio and Everything will be done by script.
8. Press Ctrl + c to stop the script and push data to DB.

