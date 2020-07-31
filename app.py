from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/welcome/',methods=["GET","POST"])
def welcome_screen():
    name=""
    print(request.form['username'])
    if(request.method=='POST'):
        name=request.form['username']
    return render_template('welcome.html',username=name)


if __name__=='__main__':
    app.run(debug=True,host="127.0.0.1",port=8000)
    