from flask import *
app= Flask(__name__)
app.secret_key="aaaa"




@app.route('/jas')
def alertinpage():
    # return "welcome to flask"
    return render_template('day2.html')
    

@app.route('/')
def emp_reg():
    return render_template('day2reg.html')


@app.route('/su',methods=['GET','POST'])
def emp_details():
    if request.method=='POST':
        res=request.form
        return render_template('day2reg_details.html',data=res)

@app.route('/cs')
def cook_set():
    res=make_response("<h1>Cookie Set</h1>")
    res.set_cookie('place','ernakulam')
    return res

@app.route('/cg')
def cook_get():
    res=request.cookies.get('place')
    return res

@app.route('/ss')
def sess_set():
    res=make_response("<h1>Session is set <a href='/sg'</a>view details</h1>")
    session['phone']=67889283
    return res
@app.route('/sg')
def sess_get():
    if 'phone' in session:
        c=session['phone']
        return 'my session value is %d    <a href="/sd">Logout</a>'%c
    else:
        return 'no session value found'

@app.route('/sd')
def sess_del():
    if 'phone' in session:
        session.pop('phone',None)
        return 'Logged out'
    else:
        return 'no session value found'

@app.route('/upld')
def emp_upload():
    return render_template('myimage.html')

@app.route('/upldsave',methods=['POST'])
def emp_upload_save():
    if request.method=='POST':
        f=request.files['img']
        f.save(f.filename)
        return 'success'



if __name__=="__main__":
    app.run(debug=True)