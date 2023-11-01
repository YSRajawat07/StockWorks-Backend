from flask import Flask, request
from flask_cors import CORS

from Custom_Input import function_test

app = Flask(__name__)

CORS(app)


@app.route('/api/endpoint', methods=['POST'])
def receive_data_from_frontend():
    data = request.get_json()
    print(data)
    # Do something with the data, e.g., process it
    # You can send a response back to the frontend
    response_data = call_function(data)
    return response_data.to_json(orient='index')


def call_function(data):
    index = data.get("index")
    dt_from = data.get("start_date")
    dt_to = data.get("end_date")
    return function_test(index, dt_from, dt_to)


if __name__ == '__main__':
    app.run(debug=True)
