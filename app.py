from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'database.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE respuestas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                mensaje TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO respuestas (nombre, correo, mensaje) VALUES (?, ?, ?)',
                       (nombre, correo, mensaje))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('formulario.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
