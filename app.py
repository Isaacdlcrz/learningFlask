import json
from dotenv import load_dotenv
from sharePlay import create_app
from sharePlay.user.model import User, User_schema

app = create_app()

try:
    load_dotenv()
except Exception as e:
    print("No .env file")

personas_feas = ['Isaac', 'Hector', 'Hectorx2']

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/getUglyPerson')
def getUglyPerson():
    try:
        res = User.query.all()
        print(res)
        return jsonify(User_schema(many = True).dump(res))
    except Exception as err:
        print(err)

@app.route('/hola', methods=['POST'])
def holaPost():
    try:
        print(json.loads(request.get_data()))
        return 'Datos agregados con éxito'
    except Exception as err:
        print(err)


if __name__ == '__main__':
    app.run(debug=True)