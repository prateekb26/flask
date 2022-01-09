from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'xyz@gmail.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def index():
    msg = Message('Hello',sender='prateek.bhat.it@gmail.com',recipients=['prat12th@gmail.com'])
    msg.body = "Hello Flask ! This message is sent from flask"
    mail.send(msg)
    return "Message sent"


if __name__ == '__main__':
    app.run(debug=True)