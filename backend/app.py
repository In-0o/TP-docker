from flask import Flask, jsonify
from flask_cors import CORS  # Ajoutez cette ligne
import os
import mysql.connector
from time import sleep

app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Configuration de la DB
def get_db():
    while True:
        try:
            return mysql.connector.connect(
                host="db",
                user="appuser",
                password="apppass",
                database="appdb"
            )
        except mysql.connector.Error as err:
            print(f"Database connection failed: {err}")
            sleep(2)

@app.route('/')
def hello():
    return jsonify(
        message="Hello from Docker!",
        environment=os.getenv('ENV', 'dev'),
        status="OK"
    )

@app.route('/data')
def get_data():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    conn.close()
    return jsonify(data=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)