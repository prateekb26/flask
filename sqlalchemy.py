from flask import Flask, request, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY.DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'random_string'
db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    pin = db.Column(db.String(100))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def index():
    return render_template("show_all.html",students=students)


@app.route('/new', methods=["POST", "GET"])
def new():
    if request.method == "POST":
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter  all the fields')
        else:
            student = students(request.form['name'],
                               request.form['city'],
                               request.form['addr'],
                               request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))

    return  render_template('new.html')


@app.route('/list')
def list_elements():
    conn = sql.connect("demo")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
