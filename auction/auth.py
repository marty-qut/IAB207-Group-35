from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect, session
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db


#create a blueprint
bp = Blueprint('auth', __name__)


# this is the hint for a login function
@bp.route('/login', methods=['GET', 'POST'])
def login(): #view function
    print('In Login View function')
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            login_user(u1)
            #nextp = request.args.get('next') #this gives the url from where the login page was accessed
            #print(nextp)
            #if next is None or not nextp.startswith('/'):
            return redirect(url_for('main.index'))
           # return redirect(nextp)
        else:
            flash(error, 'danger')
    return render_template('user.html', form=login_form, heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form_instance = RegisterForm()
    if register_form_instance.validate_on_submit():
        username = register_form_instance.user_name.data
        email = register_form_instance.email_id.data
        pwd = register_form_instance.password.data
        u = User.query.filter_by(name=username).first()

        if u:
            flash('This username already exists, please login!', 'info')
            return redirect(url_for('authentication.login'))

        pwd_hash = generate_password_hash(pwd) 
        new_user = User(name=username, emailid=email, password_hash=pwd_hash)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))

    else:
        return render_template('user.html', form=register_form_instance, heading='Register')

@bp.route('/logout')
def logout():
    session.clear()
    return render_template('authentication/logout.html')
