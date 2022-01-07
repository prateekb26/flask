from flask import Flask, request, render_template, redirect, abort, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        if request.form['username'] == "admin":
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return "logged in successfully"


if __name__ == '__main__':
    app.run(debug=True)
