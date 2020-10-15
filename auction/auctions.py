from flask import Blueprint, render_template, url_for, redirect
#from .models import Auction, Comment
#from travel.forms import AuctionForm, CommentForm
from flask_login import login_required, current_user
from . import db
import os
from werkzeug.utils import secure_filename

bp = Blueprint('auction', __name__, url_prefix = '/auctions')

@bp.route('<id>')
def show(id):
    return render_template('index.html')
