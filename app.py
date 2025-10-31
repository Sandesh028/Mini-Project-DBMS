# app.py
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

# --- Helper function ---
def get_db_connection():
    conn = sqlite3.connect('petadoption.db')
    conn.row_factory = sqlite3.Row
    return conn


# --- Routes ---
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pets')
def pets():
    conn = get_db_connection()
    pets = conn.execute('SELECT * FROM Pets WHERE status="Available"').fetchall()
    conn.close()
    return render_template('pets.html', pets=pets)


@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        breed = request.form['breed']
        age = request.form['age']
        gender = request.form['gender']
        conn = get_db_connection()
        conn.execute('INSERT INTO Pets (name, species, breed, age, gender) VALUES (?, ?, ?, ?, ?)',
                     (name, species, breed, age, gender))
        conn.commit()
        conn.close()
        return redirect('/pets')
    return render_template('add_pet.html')


@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt(pet_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        conn = get_db_connection()
        conn.execute('INSERT INTO Users (name, email, phone, address) VALUES (?, ?, ?, ?)',
                     (name, email, phone, address))
        user_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
        conn.execute('INSERT INTO Adoption_Requests (user_id, pet_id, request_date) VALUES (?, ?, ?)',
                     (user_id, pet_id, str(date.today())))
        conn.execute('UPDATE Pets SET status="Adopted" WHERE pet_id=?', (pet_id,))
        conn.commit()
        conn.close()

        return render_template('success.html')
    return render_template('adopt.html', pet_id=pet_id)


if __name__ == "__main__":
    app.run(debug=True)