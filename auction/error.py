from flask import Flask, render_template

bp = Blueprint('error', __name__)

# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("404.html")

# app name
@app.errorhandler(410)
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("410.html")

# app name
@app.errorhandler(403)
# inbuilt function which takes error as parameter
def Forbidden(e):
# defining function
  return render_template("403.html")

# app name
@app.errorhandler(500)
# inbuilt function which takes error as parameter
def errorhandler(e):
# defining function
  return render_template("500.html")
