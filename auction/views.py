from flask import Blueprint, render_template, request, session

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    #if 'email' in session:
        #s = "<h1>What's up " + session['email'] + "</h1>"
    #else:
        return render_template('index.html')
   #return s

@bp.route('/login', methods=['GET', 'POST'])
def login():

    session['email'] = request.values.get('email')

    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('login.html')

@bp.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    return render_template('watchlist.html')

@bp.route('/sell', methods=['GET', 'POST'])
def creation():
    return render_template('creation.html')

@bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return('Session has been cleared')