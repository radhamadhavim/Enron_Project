
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
    if(len(From_user) == 0 or len(TO_USER) == 0):
        	return "Please Enter a mail id"
    predicted_emails ={}
    result = To_From_dynamo.cc_prediction(From_user, TO_USER)
    if(result):
    	predicted_emails['predictions']=result
    	return jsonify(predicted_emails)
    else:
	return "please enter a valid Enron mail Id"


@application.route('/')
def start():
     #return render_template('index.html');
    return "Welcome to Enron Web Service";

    
if __name__ == '__main__':
    application.run(debug=True)


