from flask import Flask, render_template,request, redirect, url_for,jsonify

import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bpr123',
    database='mysqll'
)
cursor = db.cursor()

@app.route('/')
def index():
    # Retrieve all tasks from the database
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)
    cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
