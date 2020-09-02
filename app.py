from flask import Flask ,render_template,request,redirect,url_for,flash,jsonify
import requests
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.config['DEBUG']=True

# Here we will have global graph data structure
# Here will store the color coded nodes
# Here we will store color coded edges

nodeColor={"default":'DarkOrange',"unvisited":'DarkOrange',"processing":'DeepPink',"finished":'LightPink',"found":'LawnGreen'}

edgeColor={"default":'Red',"traversed":'Purple'}

global_graph={"node":[],"edges":[]}

@app.route('/',methods=['GET'])
def root():
    return jsonify(global_graph)

@app.route('/addNode',methods=['GET','POST'])
def addNode():
    # Here we add a node and give it a default color
    x=int(request.args.get('x',None))
    y=int(request.args.get('y',None))
    global_graph["node"].append([len(global_graph["node"]),nodeColor["default"],x,y])
    return jsonify(global_graph)

# def checkValidEdge(source,sink):

# To add an edge we send request to /addEdge?source=&&sink=
@app.route('/addEdge',methods=['POST','GET'])
def addEdge():
    source=int(request.args.get('source',None))
    sink=int(request.args.get('sink',None))
    #rest of functional part
    if source!=None and sink!=None:
        tup1=[source,sink,edgeColor['default']]
        tup2=[sink,source,edgeColor['default']]
        if tup1 not in global_graph["edges"] and tup2 not in global_graph["edges"]:
            if sink>=0 and sink<len(global_graph["node"]) and source>=0 and source<len(global_graph["node"]) and source!=sink:

                global_graph["edges"].append([source,sink,edgeColor['default']])
    #return the python graph object after jsonification
    return jsonify(global_graph)

@app.route('/removeEdge',methods=['POST','GET'])
def removeEdge():
    source=int(request.args.get('source',None))
    sink=int(request.args.get('sink',None))
    #rest of functional part
    print(source,sink)
    #return the python graph object after jsonification


    

if __name__ == "__main__":
    app.run(debug=False)
