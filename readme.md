# Real Time Opinoin Mining System

## Functions:

1. Listen Microphone
2. Convert Audio or Video to text
3. Save Quries

## How to run

1. Clone my Repo
2. Connect Microphone
3. Open CMD
4. Make a key.py file in root dir

- File format 
`python
   # Mongo DB URI
   \_mongo_uri = "URI"
   # DB Details
   \_db_name = "tenet" #databaseName
   \_db_document = "audioText" #documentName
`

5. Run `pip install requirements.txt`
6. Run `py main.py`
7. Play the Audio and Everything will be done by script.
8. Press Ctrl + c to stop the script and push data to DB.
