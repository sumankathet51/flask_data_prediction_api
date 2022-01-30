import flask
from flask import jsonify
from flask import *
from decision import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def get_processed_data(data):
    for i, item in enumerate(data):
        data[i]["id"] = i
    return data


@app.route('/api/predict', methods=['POST'])
def api_all():

    data = request.get_json()
    arr = []
    for i, item in enumerate(data):
        tmp = [[int(data[i]['marks']), int(data[i]['lab_work']), int(data[i]['attendence']),
                int(data[i]['assignment']), int(data[i]['internal_assessment']), ]]
        arr.append(tmp)
    # marks = data['marks']
    # attendence = data['attendence']
    # lab_work = data['lab_work']
    # assignment = data['assignment']
    # assessment = data['internal_assessment']
    prediction = []
    for a in arr:
        tmp = make_prediction(a)
        prediction.append(tmp)
    return jsonify(prediction)


app.run()
