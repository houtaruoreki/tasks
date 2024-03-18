from flask import Flask, g, render_template, request, redirect, session, url_for, flash, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NOT_SECRET_KEY'
DATABASE = 'diarybook.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    if not session.get('is_logged_in'):
        return redirect("/login")
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Diaries where user_id = ?""", (session['user_id'],))
    data = cur.fetchall()
    return render_template('index.html', **locals())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        cur = db.cursor()
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM Users WHERE username = ?', (username,))
        row = cur.fetchone()
        if row is not None:
            if row[1] == password:
                session['is_logged_in'] = True
                session['user_id'] = row[0]
                return redirect(url_for('index'))
            else:
                flash('Wrong Password')
        else:
            flash('Wrong Username')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        cur = db.cursor()
        username = request.form['username']
        password = request.form['password']
        cur.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        flash('Registration successful')
        return redirect(url_for('login'))
    return render_template('registration.html')


@app.route('/add_diary', methods=['POST'])
def add_diary():
    if request.method == 'POST':
        db = get_db()
        cur = db.cursor()
        user_id = session.get('user_id')

        # Get JSON data from request body
        data = request.json
        memo = data.get('memo')
        tags = data.get('tags')

        cur.execute("INSERT INTO Diaries (user_id, memo, tags) VALUES (?, ?, ?)", (user_id, memo, tags))
        db.commit()
        db.close()

        return jsonify({"message": "Diary entry added successfully"}), 200


@app.route('/delete_diary', methods=['DELETE'])
def delete_diary():
    if request.method == 'DELETE':
        db = get_db()
        cur = db.cursor()
        memo_id = int(request.get_json('memo_id')['memo_id'])

        cur.execute("""delete from Diaries where id = ?""", (memo_id,))
        db.commit()
        db.close()
        return jsonify({"message": "successfully deleted"}), 200


@app.route('/edit_diary', methods=['PUT'])
def edit_diary():
    if request.method == 'PUT':
        db = get_db()
        cur = db.cursor()
        data = request.json
        memo_id = data.get('memo_id')
        memo = data.get('memo')
        tags = data.get('tags')
        cur.execute("""update Diaries set memo = ?, tags = ? where id = ?""", (memo, tags, memo_id))
        db.commit()
        db.close()
        return jsonify("successfully edited"), 200


@app.route('/logout')
def logout():
    session.pop('is_logged_in', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
