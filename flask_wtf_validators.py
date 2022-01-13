from flask import Flask, request, flash, render_template
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        print(form.validate())
        if form.validate() == False:
            print("in here")
            flash("All fields are required")
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')

    if request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
