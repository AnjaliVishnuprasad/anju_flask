from flask import *
from flask_mail import *   #pip install flask-mail
app= Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="anjaliqisintern@gmail.com"
app.config['MAIL_PASSWORD']="pyqv lhbv frcs bpbt"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
@app.route('/m')
def send_myemail():
    msg=Message('subject',sender='anjaliqisintern@gmail.com',recipients=['tinkuanju95@gmail.com'])
    msg.body="my flask mail"
    mail.send(msg)
    return 'success'


if __name__=="__main__":
    app.run(debug=True)