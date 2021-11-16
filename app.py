from types import MethodType
from flask import Flask,jsonify,request
from tree import Tree

app = Flask(__name__)

'''
json fromat for insert
data = {
    "dim": [{
        "key": "device",
        "val": "mobile"
        },
        {
        "key": "country",
        "val": "IN"
        }],

    "metrics": [{
            "key": "webreq",
            "val": 70
            },
            {
            "key": "timespent",
            "val": 30
            }]
}

'''
'''
json format for query

query = {
    "dim": [{
        "key": "country",
        "val": "IN"
        }]
}
'''
tree = Tree()

@app.route("/")
def default():
    return "This is Default Endpoint"
    
@app.route("/v1/insert",methods=['Post'])
def insert():
    '''
    function to insert metrics
    '''
    data = request.get_json()
    tree.insert(data)
    result = {
        "status":200,
        "data":tree.data
    }
    return jsonify(result)

@app.route("/v1/query",methods = ['Get'])
def get():
    '''
    function to get metrics
    '''
    query = request.get_json()  
    try:
        result = tree.get(query)
        return jsonify(result)
    except:
        return "No Data Found"
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
