from flask import Flask, request, render_template
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/enternew')
def new_student():
    return render_template('sqlstudent.html')


@app.route('/addrec', methods=["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("demo") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES(?,?,?,?)", (nm, addr, city, pin))
                conn.commit()
                msg = "Record inserted successfully"
        except:
            conn.rollback()
            msg = "Error!!! Inserting record successfully"
        finally:
            conn.close()
            return render_template('sqlresult.html', msg=msg)


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
