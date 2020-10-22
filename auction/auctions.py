from flask import Blueprint, render_template, url_for, redirect
from .models import Auction, Bid
from .forms import AuctionForm, BidForm
from flask_login import login_required, current_user
from . import db
import os
from werkzeug.utils import secure_filename

bp = Blueprint('auction', __name__, url_prefix = '/auctions')

@bp.route('/<id>')
def listing(id):
    auction = Auction.query.filter_by(id=id).first()
    bid_form_instance = BidForm()
    return render_template('auctions/listing.html', auction=auction, form=bid_form_instance)

@bp.route('/<id>/bid', methods=['GET', 'POST'])
@login_required
def bid(id):
    bid_form_instance = BidForm()
    auction_obj = Auction.query.filter_by(id=id).first()
    if bid_form_instance.validate_on_submit():

        bid = Bid(text=bid_form_instance.bid.data,
                          auction=auction_obj,
                          user=current_user)
        
        db.session.add(bid)
        db.session.commit()
    return redirect(url_for('auction.listing', id=id))

def check_upload_file(form):
  fp = form.image.data
  filename = fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))

  db_upload_path = '/static/image/'+ secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

@bp.route('/sell', methods=['GET', 'POST'])
@login_required
def create():
  auction_form_instance = AuctionForm()
  if auction_form_instance.validate_on_submit():

    db_file_path = check_upload_file(auction_form_instance)
    
    auction = Auction(model=auction_form_instance.model.data,   
                              name=auction_form_instance.name.data,
                              description=auction_form_instance.description.data,
                              image=db_file_path)

    db.session.add(auction)
    db.session.commit()
    
    print('form is valid')
    return redirect(url_for('auction.create'))

  return render_template('auctions/creation.html', form=auction_form_instance)

