from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required
from .models import Auction

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    auctions = Auction.query.all()
    return render_template('index.html', auctions=auctions)

@bp.route('/search')
def search():
    if request.args['search']:
        auct = "%" + request.args['search'] + '%'
        auctions = Auction.query.filter(Auction.model.like(auct)).all()
        return render_template('index.html', auctions=auctions)
    else:
        return redirect(url_for('main.index'))

@bp.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():
    return render_template('watchlist.html')

@bp.route('/sell', methods=['GET', 'POST'])
@login_required
def creation():
    return render_template('creation.html')

