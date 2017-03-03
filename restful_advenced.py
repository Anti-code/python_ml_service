from flask import Flask,jsonify,request,abort,make_response
import flask
import json

app = Flask(__name__)

int_paginationVal = 1
people_list = []
people_len = None

def _loadpeople():
    global people_list,people_len
    with open('people.json','r') as data_file:    
        data = json.load(data_file)
        people_list = data['people']
        people_len = len(people_list)
        #print(str(data)+str(people_len))

@app.route('/')
def index():
    return "Hello, World!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'errorCode': 'Not found'}), 404)

@app.route('/people/api/v1.0/getpeople')
def getAllpeople():
    resp = jsonify( {"people": people_list} )
    return resp

@app.route('/people/api/v1.0/getpeople/<int:beg>',methods=['GET'])
def getSomepeople(beg):
    if( beg not in range(people_len)):
        abort(404)
    intSize = None
    try:
        intSize = int(request.args.get('size'))
    except Exception as e:
        print('Invalid size argument')
    if intSize:
        #To return next value header 
        int_nextVal = beg+intSize
    else:
        #Use default pagination value if not specified by the user
        int_nextVal = beg+int_paginationVal
    resp = jsonify( {"people": people_list[beg:][:(int_nextVal-beg)]} )
    if int_nextVal >= len(people_list):
        resp.headers['Next-Val'] = -1
    else:
        resp.headers['Next-Val'] = int_nextVal
    return resp

if __name__ == '__main__':
    _loadpeople()
    app.run(debug=True)