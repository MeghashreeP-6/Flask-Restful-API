from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

def checkstatuscode(functionname, posteddata): 
    if (functionname == "add" or functionname == "sub" or functionname == "mul"):
        #nan = (math.isnan(float(posteddata['x']))or math.isnan(float(posteddata['y'])))
        if "x" not in posteddata or "y" not in posteddata:
            return 301
        elif type(posteddata['x']) == str or type(posteddata['y']) == str:
            return 400
        else:
            return 200
    elif functionname == "div":
        if "x" not in posteddata or "y" not in posteddata:
            return 301
        elif type(posteddata['x']) == str or type(posteddata['y']) == str:
            return 400
        elif int(posteddata['y']) == 0:
            return 302
        else:
            return 200
        
class Add(Resource):
    def post(self):
        post_data = request.get_json()

        status_code = checkstatuscode("add", post_data)

        if status_code !=200:
            if status_code == 400:
                retMap = {
                    "Message" : "Not a number",
                    "Status Code" : 400 
                }
                return retMap
            else:
                retMap = {
                    "Message" : "Value not provided",
                    "Status Code" : 301 
                }
            return retMap
        
        x = post_data['x']
        y = post_data['y']

        x = int(x)
        y = int(y)
        ret = x + y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return retMap


class Subtract(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = checkstatuscode("sub", posted_data)

        if status_code !=200:
            if status_code == 400:
                retMap = {
                    "Message" : "Not a number",
                    "Status Code" : 400 
                }
                return retMap
            else:
                retMap = {
                    "Message" : "An error occured",
                    "Status Code" : 301 
                }
            return retMap
        
        x = posted_data['x']
        y = posted_data['y']

        x = int(x)
        y = int(y)
        diff = x-y
        
        retMap = {
            'Message': diff,
            'Status Code': 200
        }
        return retMap



class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = checkstatuscode("mul", posted_data)

        if status_code !=200:
            if status_code == 400:
                retMap = {
                    "Message" : "Not a number",
                    "Status Code" : 400 
                }
                return retMap
            else:
                retMap = {
                    "Message" : "An error occured",
                    "Status Code" : 301 
                }
                return retMap
        
        x = posted_data['x']
        y = posted_data['y']

        x = int(x)
        y = int(y)
        timesof = x*y
        
        retMap = {
            'Message': timesof,
            'Status Code': 200
        }
        return retMap

class Divide(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = checkstatuscode("div", posted_data)

        if status_code !=200:
            if status_code == 400:
                retMap = {
                    "Message" : "Not a number",
                    "Status Code" : 400 
                }
                return retMap
            elif status_code == 302:
                retMap = {
                    "Message" : "Divide by zero error",
                    "Status Code" : 302 
                }
            else:
                retMap = {
                    "Message" : "An error occured",
                    "Status Code" : 301 
                }
            return retMap
        
        x = posted_data['x']
        y = posted_data['y']

        x = int(x)
        y = int(y)
        value = (x*1.0)/y
        
        retMap = {
            'Message': value,
            'Status Code': 200
        }
        return retMap

api.add_resource(Add,'/add')
api.add_resource(Subtract,'/sub')
api.add_resource(Multiply,'/mul')
api.add_resource(Divide,'/div')

if __name__=="main":
    app.run(debug=True)