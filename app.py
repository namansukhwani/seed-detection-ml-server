# import numpy as np
# import cv2
# import requests as fetch
# from PIL import Image
# from io import BytesIO
# from keras.models import load_model
# model = load_model('multiclass_model80_77.h5')
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#flask imports
from flask import Flask
from flask_restful import Api, Resource,abort,request
# from os import environ

# SERVICE_SUBSCRIPTION_KEY=environ.get('SERVICE_SUBSCRIPTION_KEY')

#Flask initialization
app=Flask(__name__)
api=Api(app)

#ML Functions

#Flask validation functions

# def req_validation(body):
#     if "subscriptionKey" not in body:
#         abort(400,status=False,message="request parameters missing")
#     elif str(body['subscriptionKey'])!=SERVICE_SUBSCRIPTION_KEY:
#         abort(400,status=False,message="Invalid username or password")

# #Flask responce class        
            
# def urlToImage(url):
#     with open('tempImage.jpg', 'wb') as f:
#         f.write(fetch.get(url).content)
#     image=Image.open('tempImage.jpg')
#     new_image=image.resize((128,128))
#     new_image.save('finalImg.jpg')
#     return 'finalImg.jpg'
    

# def pred(url):
#     # image=Image.open('img2.jpg')
#     # new_image=image.resize((128,128))
#     # new_image.save('finalImg.jpg')
#     k = np.expand_dims(cv2.imread(urlToImage(url))*(1.0/255.0), axis=0)
#     p = model.predict(k)
#     a = np.argmax(p)
#     return {"totalQuality":a,"data":p}

class SeedQuality(Resource):
    def post(self):
        req_json=request.get_json(force=True)

        # req_validation(req_json)
        
        url=req_json['url']
        
        # result=pred(url)

        return{
            "status":True,
            "message":"responce sucessful",
            "data":"2",
            "imageUrl":url
        },200


#Flask paths
api.add_resource(SeedQuality,'/getQuality')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=False)