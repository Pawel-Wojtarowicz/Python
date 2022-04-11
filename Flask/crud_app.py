import mysql.connector
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import jsonpickle


def get_connection_to_db():
    connection = mysql.connector.connect(
        user='root', password='pawel', host='localhost', database='python', auth_plugin='mysql_native_password')
    return connection


app = Flask(__name__)


class User:
    def __init__(self, user_id, username, city):
        self.user_id = user_id
        self.username = username
        self.city = city


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    connection = get_connection_to_db()
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT id, username, city FROM users'
    cursor.execute(query)

    for row in cursor:
        users.append(User(row['id'], row['username'], row['city']))

    connection.close()

    response = Response(jsonpickle.encode(
        users, unpicklable=False), mimetype='application/json')

    return response


@app.route('/users/', methods=['POST'])
def add_user():
    request_data = request.get_json()

    try:
        connection = get_connection_to_db()
        cursor = connection.cursor()

        query = 'INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(status=err.msg), 400
    finally:
        connection.close()

    return request_data, 201


app.run()
