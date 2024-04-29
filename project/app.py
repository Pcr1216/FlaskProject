from flask import Flask, render_template, app

app=Flask(__name__)

@app.route("/",methods=['GET'])
def getHome():
    return render_template('home.html')

@app.route("/account",methods=['GET'])
def getAcc():
    return render_template('account.html')


if __name__=='__main__':
    app.run(debug=True)
