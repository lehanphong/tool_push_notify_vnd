# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

import requests
from flask import Flask, request

app = Flask(__name__)

key = 'FIREBASE_KEY'
firebase_key = os.getenv(key)

@app.route("/")
def hello_world():
    return "<p>Tool post notify for mobile</p>"


@app.route('/send_notify', methods=['POST'])
def send_notify():
    if request.method == 'POST':
        dic_json = request.json
        url = 'https://fcm.googleapis.com/fcm/send'
        print(dic_json)
        json_data = json.dumps(dic_json)
        print(json_data)
        x = requests.post(url, data=json_data, headers={'Content-Type':'application/json','Authorization': 'key={0}'.format(firebase_key)})
        print("res code" + str(x.status_code))
        print("res code" + x.text)
        response = app.response_class(
            response=json.dumps(x.json()),
            status=x.status_code,
            mimetype='application/json'
        )
        return response





