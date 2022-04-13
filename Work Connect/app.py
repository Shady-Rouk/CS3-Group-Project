from flask import Flask, render_template, request, url_for, redirect, session, request, redirect

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods = ['GET','POST']) 
def home():
    if request.method == 'POST':
        result = request.form['scope'] #result is the user's search entry for a job scope
        new_route = f'/result/{result}'
        return redirect(new_route)
    else:
        return render_template("index.html")


@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/result/<scope>", methods=['GET', 'POST'])
def result(scope):
    if request.method == 'GET':
        #render result template with values gotten from db for 'scope'
        return render_template("result.html", scope=scope)


    
if __name__ == "__main__": 
    app.run(debug = True)