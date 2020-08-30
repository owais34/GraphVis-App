from flask import Flask ,render_template,request,redirect,url_for,flash
import requests

app=Flask(__name__)
app.config['DEBUG']=True

# Here we will have global graph data structure
# Here will store the color coded nodes
# Here we will store color coded edges

@app.route('/addNode',methods=['GET','POST'])
def addNode():
    # Here we add a node and give it a default color

# To add an edge we send request to /addEdge?source=&&sink=
@app.route('/addEdge',methods=['POST','GET'])
def addEdge():
    source=request.args.get('source',None)
    sink=request.args.get('sink',None)
    #rest of functional part
    
    #return the python graph object after jsonification

@app.route('/removeEdge',methods=['POST','GET'])
def removeEdge():
    source=request.args.get('source',None)
    sink=request.args.get('sink',None)
    #rest of functional part
    
    #return the python graph object after jsonification


    

if __name__ == "__main__":
    app.run(debug=False)
