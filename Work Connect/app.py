from flask import Flask, render_template, request, url_for, redirect, session 

app = Flask(__name__) 

@app.route("/", methods = ["GET"]) 
def index(): 
    return render_template("index.html") 
    
@app.route("/home/", methods = ["GET"]) 
def home(): 
    return redirect(url_for("index")) 

@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")
    
    
if __name__ == "__main__": 
    app.run(debug = True)