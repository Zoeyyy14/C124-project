from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route("/")
def hello():
    return "Zoey"
tasks=[
    {
    "id":1,
    "name":"Zoey",
    "contact":"123498765",
    "done":False
},
 {
    "id":2,
    "name":"Python",
    "contact":"980765",
    "done":False
}
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },404)

    task={
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Task added successfuly"
        })
@app.route("/get-data")  
def get_task():
    return jsonify({
        "data":tasks,
    })  

if __name__=="__main__":
    app.run()