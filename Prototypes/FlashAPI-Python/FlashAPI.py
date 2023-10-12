from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)

def get_json(file_name):
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
        return data.get("receipts", [])


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/Recipt:<string:Name>/<int:Step>/')
def GetDate(Name,Step):
    data = get_json("C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/FlashAPI-Python/recipts.json")[Name]
    return  jsonify(data[Step])

#Use this one if you want someone else not on your machine to use it
#app.run(host='Your Local Ip address')

app.run()
#http://127.0.0.1:5000/Recipt:pancake/0/