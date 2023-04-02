import os
from flask import Flask, abort, request
from constants import DATA_DIR
from processing import filter_in_cmd1, map_in_cmd1, sort_in_cmd1, limit_in_cmd1

app = Flask(__name__)


@app.route("/perform_query/", methods=["POST"])
def perform_query():
    try:
        cmd1 = request.args.get('cmd1') or request.json.get('cmd1')
        value1 = request.args.get('value1') or request.json.get('value1')
        cmd2 = request.args.get('cmd2') or request.json.get('cmd2')
        value2 = request.args.get('value2') or request.json.get('value2')
        file_name = request.args.get('file_name') or request.json.get('file_name')
        log_file = os.path.join(DATA_DIR, file_name)
        if not os.path.isfile(log_file):
            abort(400, 'Ошибка. Имя имя файла не несоответствует')
        elif cmd1 == 'filter':
            return filter_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'map':
            return map_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'sort':
            return sort_in_cmd1(cmd1, cmd2, value1, value2)
        elif cmd1 == 'limit':
            return limit_in_cmd1(cmd1, cmd2, value1, value2)
        else:
            abort(400, 'Введенные данные недопустимы')
    except Exception as e:
        abort(400, e)
