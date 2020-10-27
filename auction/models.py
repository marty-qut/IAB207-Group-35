from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    bids = db.relationship('Bid', backref='user')
    auctions = db.relationship('Auction', backref='user')
    watchlists = db.relationship('Watchlist', backref='user')



class Auction(db.Model):
    __tablename__ = 'auctions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    model = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    starting_bid = db.Column(db.String(400))
    auction_status = db.Column(db.String(400))
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    bids = db.relationship('Bid', backref='auction')
    watchlists = db.relationship('Watchlist', backref='auction')
    #add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    auction_id = db.Column(db.Integer, db.ForeignKey('auctions.id'))
    #watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlist.id'))

    def __repr__(self):
        return "{}".format(self.text)


class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    #add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    auction_id = db.Column(db.Integer, db.ForeignKey('auctions.id'))
	
    def __repr__(self): #string print method
        return "<Watchlist: {}>".format(self.name)