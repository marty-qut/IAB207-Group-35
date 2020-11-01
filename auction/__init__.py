#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():

    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='utroutoru'
    #set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketplace.sqlite'
    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    #initialize the login manager
    login_manager = LoginManager()

    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #importing views module here to avoid circular references
    # a commonly used practice.

    from . import views
    app.register_blueprint(views.bp)

    from . import auctions
    app.register_blueprint(auctions.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    # error handling
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error/forbidden.html', title = '403'), 403
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/pagenotfound.html', title = '404'), 404
    @app.errorhandler(410)
    def page_gone(error):
        return render_template('error/gone.html', title = '410'), 410
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/internalservererror.html', title = '500'), 500

    app.register_error_handler(403, forbidden)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(410, page_gone)
    app.register_error_handler(500, internal_error)

    return app
