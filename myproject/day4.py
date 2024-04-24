from flask import *
import sqlite3
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///anjali.sqlite3'
app.config['SECRET_KEY']='abc'
db=SQLAlchemy(app)

class Employees(db.Model):
    id=db.Column('employee_id',db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address

@app.route('/add',methods=['GET','POST'])
def add_emp():
    if request.method=='POST':
        # return 'success'
        em=Employees(request.form['name'],request.form['address'])
        db.session.add(em)
        db.session.commit()
        return redirect(url_for('display'))

    else:
        return render_template('add_emp.html')

@app.route('/')
def display():
    return render_template('list_emp.html',emp=Employees.query.all())

@app.route('/delete/<int:id>/',methods=['GET','POST'])
def del_emp(id):
    em=Employees.query.get(id)
    db.session.delete(em)
    db.session.commit()
    return redirect(url_for('display'))

@app.route('/update/<int:id>/',methods=['GET','POST'])
def update_employee(id):
    em = Employees.query.get(id)

    if request.method == 'POST':
        em.name = request.form['name']
        em.address = request.form['address']
        db.session.commit()
        return redirect(url_for('display'))
    return render_template('update_emp.html', employee=em)


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)