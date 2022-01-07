from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/')
def index():
    if "username" in session:
        username = session["username"]
        return "Logged in as " + username + "<br>" + \
               "<b><a href ='/logout'> Click here to logout</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in </b></a>"


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
