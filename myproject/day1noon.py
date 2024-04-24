from flask import *
app= Flask(__name__)


@app.route('/a')
def admin():
    return 'ADMIN'

@app.route('/t')
def teacher():
    return 'TEACHER'

@app.route('/s')
def student():
    return 'STUDENT'


@app.route('/user/<name>')
def user(name):
    if name=="admin":
        return redirect(url_for('admin'))
    if name=="teacher":
    # if name=="tea": (this too will work)
        return redirect(url_for('teacher'))
    if name=="student":
        return redirect(url_for('student'))

# @app.route('/page')
# def mypage():
#     return render_template('day1.html')

# @app.route('/page/<uname>')
# def mypage(uname):
#     return render_template('day1.html',name=uname)


@app.route('/t/<int:num>')
def mytable(num):
    return render_template('day1.html',n=num,name="Multiplication table of ")

# @app.route('/login',methods=['GET'])
# def reg():
#     uname=request.args.get('fname')
#     place=request.args.get('pl')
#     return 'success'+uname

@app.route('/login',methods=['POST'])
def reg():
    print('.................................')
    uname=request.form['fname']
    place=request.form['pl']
    return 'success '+uname

if __name__=="__main__":
    app.run(debug=True)