import os

from flask import Flask, request, jsonify
from constants import DATA_DIR
from marshmallow import ValidationError
from schema import RequestJsonSchema
from functions import get_query

app = Flask(__name__)

@app.route("/perform_query/", methods=["POST"])
def perform_query():
    try:
        data = RequestJsonSchema().load(request.json)
    except ValidationError:
        return f'Request is incorrect', 500

    values_cmd = ['sort', 'filter', 'limit', 'map', 'unique']

    try:
        if data['cmd1'] not in values_cmd or data['cmd2'] not in values_cmd:
            raise ValidationError
    except ValidationError:
        return f'cmd functions are not correct', 500

    with open(os.path.join(DATA_DIR, data['file_name'])) as result:
        result = get_query(data['cmd1'], data['value1'], result)
        result = get_query(data['cmd2'], data['value2'], result)

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(port=25000, debug=True)
