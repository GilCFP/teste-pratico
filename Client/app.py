from utils import isweekday, findbetterprice, getallids, getsingledata, getsingleprice, checkpassword
from flask import Flask, request, render_template,jsonify
from classes import WrongPasswordError

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/api/search', methods = ['POST'])
def findthebestprice():

    #Request data
    data = request.get_json()

    try:

        #Makes a password check and then return the best option
        checkpassword(data["password"])
        return findbetterprice([getsingleprice(id = id ,weekday= isweekday(day = data['day'], month = data['month'], year=data['year']), quantity= data["quantity"]) for id in getallids()])

    #Exceptions
    except ValueError as e:
        e = str(e)
        return jsonify({'error':e}), 400

    except WrongPasswordError as e:
        e = str(e)
        return jsonify({'error': e}), 401

    except KeyError:
        e = str(e)
        return jsonify({'error': "A requisição não possui todas as informações necessárias e/ou não está no formato correto"}),400

if __name__ == '__main__':
    app.run(debug=True)