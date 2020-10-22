# class Profile

class Profile:
    def __init__(self, user_id, name, email, password, date_joined):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.date_joined = date_joined

    def __repr__(self):
        str = 'Username: {0} \n Date Joined: {1} '
        str.format(self.name, self.date_joined)
        return str

# class Item

class Item:
    def __init__(self, user_id, item_id, name, description, image):
        self.owner = user_id
        self.id = item_id
        self.name = name
        self.description = description
        self.image = image


    def __repr__(self):
        str = 'Name: {0} Currency: {1}'
        str.format(self.name, self.currency)
        return str

# class Auction

class Auction:
    def __init__(self, user_id, item_id, auction_id, name, description, currency):
        self.owner = user_id
        self.item = item_id
        self.id = auction_id
        self.description = description
        self.currency = currency
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

    def __repr__(self):
        str = 'Auctioned item: {0}\n Price: {1}'
        str.format(self.name, self.currency)
        return str

# class Bid

class Bid:
    def __init__(self, user_id, auction_id, description, currency):
        self.owner = user_id
        self.auction = auction_id
        self.description = description
        self.currency = currency

    def __repr__(self):
        str = 'User {0} bid Currency {1} with description {2}'
        str.format(self.name, self.currency, self.description)
        return str

# class Comment

class Comment:
    def __init__(self, user_id, contents, date_added):
        self.owner = user_id
        self.contents = contents
        self.dateadded = date_added

    def __repr__(self):
        str = '{0} says\n{1}\nOn {2}'
        str.format(self.name, self.contents, self.dateadded)
        return str

# class Watchlist:

class Watchlist:
    def __init__(self, user_id, item_id):
        self.user = user_id
        self.item = item_id

    def __repr__(self):
        str = 'User {0} has item {1} watchlisted'
        str.format(self.user, self.item)
        return str
