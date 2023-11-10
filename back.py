from flask import Flask
from flask_cors import CORS
from flask import request
import retrieve_quizz


app = Flask(__name__)
CORS(app)

@app.route('/quizzes')
def get_quizzes():
    quizzes = retrieve_quizz.get_quizzes()
    return (quizzes)

@app.route('/quizz/<id>')
def get_quizz(id):
    quizz = retrieve_quizz.get_quizz(id)
    return quizz

@app.route('/random_quizz/<difficulty>', methods=['POST'])
def create_random_quizz(difficulty):
    data = request.json 
    print("data:")
    print(data)
    print(data["ultiOnly"])
    quizz = retrieve_quizz.create_random_quizz(difficulty)
    return quizz


if __name__ == '__main__':
    app.run()