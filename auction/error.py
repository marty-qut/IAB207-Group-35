from flask import Flask, render_template

bp = Blueprint('error', __name__)

# app name
@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
  return render_template("404.html")
