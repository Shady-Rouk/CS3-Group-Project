from flask import Flask, render_template, request, url_for, redirect, session, request, redirect
from model import get_details_from_db

app = Flask(__name__) 

@app.route("/", methods = ['GET','POST'])
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
        scope = scope.lower()
        companies = get_details_from_db(scope)
        #render result template with values in 'companies' from db for 'scope'
        # scope = "tech"
        # a = get_details_from_db(scope)
        # for company in a:
        #     print(company['company_name'].capitalize())
        #     print("link: " + company["job_scope"][scope])
        #sample use case
        return render_template("result.html", scope=scope, companies=companies)


    
if __name__ == "__main__": 
    app.run(debug = True)