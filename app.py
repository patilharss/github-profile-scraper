from flask import Flask,render_template,request,redirect
from scraper import getDetails
app=Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/submit',methods=['POST'])
def submit():
    username=""
    if request.method == 'POST':
        username=request.form['username']
        data=getDetails(str(username))
        # print(data)
        return render_template('index.html',username=data)

