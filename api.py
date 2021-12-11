import flask
from flask import jsonify
from flask import request
from decision import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

test_data = [
    [3, 1, 1, 0, 1],
]


@app.route('/api/predict', methods=['POST'])
def api_all():

    data = request.get_json()
    marks = data['marks']
    attendence = data['attendence']
    lab_work = data['lab_work']
    assignment = data['assignment']
    assessment = data['internal_assessment']
    data = [
        [marks, attendence, lab_work, assignment, assessment]
    ]
    prediction = make_prediction(data)
    # print(prediction)
    return jsonify(prediction)


app.run()
