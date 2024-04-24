from flask import Flask
app= Flask(__name__)#creating a flask class obj



@app.route('/') #url mapping associated with the function  syntax: app.route(rule,option)
def home():
    # return "welcome to flask"
    return "<h1>Haii</h1>"


@app.route('/hai/<myname>')
def details(myname):
    return 'my name is '+myname


@app.route('/hai/<int:num>')
def mynum(num):
    return 'my number is %d'%num



def myhome():
    return 'my home page'

app.add_url_rule("/myhome","myhome",myhome)

if __name__=="__main__":
    app.run(debug=True)