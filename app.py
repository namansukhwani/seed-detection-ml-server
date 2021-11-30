# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# import pickle
# import numpy as np

# from keras.models import load_model
# model = load_model('chatbot_model.h5')
# import json
# import random
# intents = json.loads(open('intents.json').read())
# words = pickle.load(open('words.pkl','rb'))
# classes = pickle.load(open('classes.pkl','rb'))

#flask imports
from flask import Flask
from flask_restful import Api, Resource,abort,request
from os import environ

SERVICE_SUBSCRIPTION_KEY=environ.get('SERVICE_SUBSCRIPTION_KEY')

#Flask initialization
app=Flask(__name__)
api=Api(app)

#ML Functions

#Flask validation functions

def req_validation(body):
    if "subscriptionKey" not in body:
        abort(400,status=False,message="request parameters missing")
    elif str(body['subscriptionKey'])!=SERVICE_SUBSCRIPTION_KEY:
        abort(400,status=False,message="Invalid username or password")

#Flask responce class

class SeedQuality(Resource):
    def post(self):
        req_json=request.get_json()

        req_validation(req_json)

        data=str(req_json['data'])

        return{
            "status":True,
            "message":"chatbot responce sucessful",
            "data":{}
        },200


#Flask paths
api.add_resource(SeedQuality,'/getQuality')

if __name__=="__main__":
    app.run(host="0.0.0.0")