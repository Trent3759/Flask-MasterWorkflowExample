"""
Project: Flask-MasterWorkflowExample
Description: See project readme. 
Notes:
"""
#==============================Imports=======================================
import sys

from flask import Flask, render_template, request as flask_request, make_response, redirect, url_for, abort

app = Flask(__name__)

#==========================Global Variables==================================

ip_address = "0.0.0.0"

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
	return render_template("master.html")

@app.route("/<route>")
def page(route):
    return render_template("master.html", page2load=route)

@app.route("/page/<route>")
def half(route):
    try:
        return render_template(route + ".html")
    except:
        abort(404) 

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html") 

#==========================Main========================================

def main():
		app.run(host='',port=8080)
if(__name__ == "__main__"):
		main()
