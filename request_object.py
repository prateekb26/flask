from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def student():
    return render_template("student.html")

@app.route('/result', methods=["POST","GET"])
def result():
    if request.method == "POST":
        results = request.form
        return render_template("result.html", result=results)


if __name__ == '__main__':
    app.run(debug=True)
