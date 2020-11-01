from flask import Blueprint, render_template, url_for, redirect, flash
from .models import Auction, Bid, Watchlist
from .forms import AuctionForm, BidForm, CloseForm, WatchlistForm
from flask_login import login_required, current_user
from . import db
import os
from werkzeug.utils import secure_filename

bp = Blueprint('auction', __name__, url_prefix = '/auctions')

@bp.route('/<id>')
def listing(id):
    auction = Auction.query.filter_by(id=id).first()

    close_form_instance = CloseForm()
    bid_form_instance = BidForm()
    add_form_instance = WatchlistForm()

    return render_template('auctions/listing.html', auction=auction, form=bid_form_instance, form2=close_form_instance, form3=add_form_instance)


@bp.route('/<id>/bid', methods=['GET', 'POST'])
@login_required
def bid(id):
    auction_obj = Auction.query.filter_by(id=id).first()
    bid_form_instance = BidForm()

    if db.session.query(Bid.text).filter_by(auction_id=id).order_by(Bid.id.desc()).first() != None: # This looks for any existing entries in the Bid table in the database
      last_bid = db.session.query(Bid.text).filter_by(auction_id=id).order_by(Bid.id.desc()).first() # The query to find the latest bid
      last_bid = str(last_bid) # Convert the query into a string
      last_bid = last_bid.translate({ord(i): None for i in "(),''"}) # Remove the funky weirdness that's returned by a query
      last_bid = int(last_bid) # Convert the query into an integer, which will just be the bare number entered.
    else: 
      last_bid = db.session.query(Auction.starting_bid).filter_by(id=id).first()
      last_bid = str(last_bid)
      last_bid = last_bid.translate({ord(i): None for i in "(),''"})
      last_bid = int(last_bid)
      # If it doesn't find any bids, it will adjust to using the starting bid and then completes the same process. 
      # Could probably turn this into a definition to remove the repeatable code but it works as is and I don't want to screw with it

    if bid_form_instance.validate_on_submit():

        if bid_form_instance.bid.data > last_bid: # Compares the bid entered by the user with the bid already existing from the if statement above

          bid = Bid(text=bid_form_instance.bid.data,
                                auction=auction_obj,
                                user=current_user)

          db.session.add(bid)
          db.session.commit()

          print('form is valid')

        else:
          flash('Please bid a value higher than the previous bid', 'info') # When the user tries to enter a bid number lower than the latest stored bid
    else:
      flash('Please enter a number for your bid', 'info') # When the user tries to enter anything that isn't accepted by the flaskform
      
    return redirect(url_for('auction.listing', id=id))

@bp.route('/<id>/add', methods=['GET', 'POST'])
@login_required
def addlist(id):
    auction = Auction.query.filter_by(id=id).first()
    add_form_instance = WatchlistForm()

    if add_form_instance.validate_on_submit():
      watchlist = Watchlist(auction=auction,
                            user=current_user)
      
      db.session.add(watchlist)
      db.session.commit()

      flash('Item added to your watchlist', 'info')

    return redirect(url_for('auction.listing', id=id))

@bp.route('/<id>/close', methods=['GET', 'POST'])
def closeauction(id):
    auction = Auction.query.filter_by(id=id).first()
    close_form_instance = CloseForm()
    status_number = 1

    if close_form_instance.validate_on_submit():
      auction.auction_status = status_number

      db.session.commit()

    return redirect(url_for('auction.listing', id=id))
# Closing an auction is simply setting its respective field in the database to a value other than null, then using IF statements to see if this is true or false

def check_upload_file(form):
  fp = form.image.data
  filename = fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))

  db_upload_path = '/static/image/'+ secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path
# Necessary code from tutes to get images working

@bp.route('/sell', methods=['GET', 'POST'])
@login_required
def create():
  auction_form_instance = AuctionForm()
  if auction_form_instance.validate_on_submit():

    db_file_path = check_upload_file(auction_form_instance)
    
    auction = Auction(model=auction_form_instance.model.data,   
                              name=auction_form_instance.name.data,
                              description=auction_form_instance.description.data,
                              image=db_file_path,
                              starting_bid=auction_form_instance.starting_bid.data,
                              user=current_user)

    db.session.add(auction)
    db.session.commit()
    
    print('form is valid')
    flash('Item successfully listed', 'info')
    return redirect(url_for('auction.create'))

  return render_template('auctions/creation.html', form=auction_form_instance)
