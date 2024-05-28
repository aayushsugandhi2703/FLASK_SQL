from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '\xbd\xa4\xe9_4[!\xe5oW\xc9\xfc\xdfM+\xaf\x9b\x88my\xd6\xfe\xd9T'  # Replace with your own secret key

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
        return render_template('index.html', tasks=tasks, task="TASK WEBPAGE")

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['task']
        description = request.form['description']
        complete = request.form.get('complete', False)
        
        try:
            # Insert data into the database
            cursor.execute('INSERT INTO tasks (title, description, complete) VALUES (%s, %s, %s)', (title, description, complete))
            db.commit()
            flash('Task added successfully')
        except Exception as e:
            db.rollback()
            flash(f'Error adding task: {str(e)}')
        
        return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['task']
        description = request.form['description']
        complete = request.form.get('complete', False)
        
        try:
            # Update data in the database
            cursor.execute('UPDATE tasks SET title=%s, description=%s, complete=%s WHERE id=%s', (title, description, complete, id))
            db.commit()
            flash('Task updated successfully')
        except Exception as e:
            db.rollback()
            flash(f'Error updating task: {str(e)}')
        
        return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        try:
            # Delete task from the database
            cursor.execute('DELETE FROM tasks WHERE id = %s', (id,))
            db.commit()
            flash('Task deleted successfully')
        except Exception as e:
            db.rollback()
            flash(f'Error deleting task: {str(e)}')
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
