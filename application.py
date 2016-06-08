
from flask import Flask,url_for,request,render_template,jsonify

import re
import csv
import random
import json
import To_From_dynamo

application = Flask(__name__)

@application.route('/predict', methods=['GET'])
def predict():
    From_user = request.args.get('from')
    TO_USER = request.args.get('to')
    predicted_emails ={}
    result = To_From_dynamo.cc_prediction(From_user, TO_USER)
    predicted_emails['predictions']=result
    return jsonify(predicted_emails)


@application.route('/')
def start():
    return "Welcome to Enron Web Service";

    
if __name__ == '__main__':
    application.run(debug=True)


