from flask import Flask, render_template, request, url_for, redirect, session, request

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods = ['GET','POST']) 
def home():
    if request.method == 'POST':
        result = request.form['scope'] #result is the user's search entry for a job scope
        return render_template("result.html")
    else:
        return render_template("index.html")


@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return render_template("result.html")


    
if __name__ == "__main__": 
    app.run(debug = True)