from flask import Flask,render_template,request,redirect
from scraper import getDetails
app=Flask(__name__)

@app.route('/')
def main():
    print('hello')
    return render_template("index.html")

@app.route('/submit',methods=['POST'])
def submit():
    username=""
    if request.method == 'POST':
        username=request.form['username']
        data=getDetails(str(username))
        print('----------------------------')
        print((data))
        return render_template('index.html',username=data)

if __name__ == '__main__':
    app.run(debug=True)