from flask import Flask, jsonify, request
import json
from dotenv import load_dotenv
# from model.model import db, ma 
from user.model import User, User_schema

app = Flask(__name__)

try:
    load_dotenv()
except Exception as e:
    print("No .env file")

personas_feas = ['Isaac', 'Hector', 'Hectorx2']

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/getUglyPerson/<index>')
def getUglyPerson(index):
    try:
        res = {
            'ugliest_person': personas_feas[int(index)]
        }

        return jsonify(res)
    except Exception as err:
        # print(err)
        pass

@app.route('/hola', methods=['POST'])
def holaPost():
    try:
        print(json.loads(request.get_data()))
        return 'Datos agregados con éxito'
    except Exception as err:
        print(err)


if __name__ == '__main__':
    app.run(debug=True)