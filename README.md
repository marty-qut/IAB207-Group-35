# IAB207-Group-35
# List changes you do here:

# 13/10:
# Directory has been updated to include the assessment skeleton structure. - Toby

# 14/10:
# Sorted out old html files into a subfolder for posterity, can now run main.py python file in terminal to get a browser version of the site that  loosely works to a week 7/very little week 8 standard. Each page uses the {% extend base.html %} method to automatically generate headings and footers from a template. - Toby

# 15/10
# Quickly added an auctions.py file which will replicate what the destinations.py file did for the workshop website.

# 18/10
# Made authenticated routing possible + used basic wtforms to set up login, register and logout pages to a week 8 standard. Sorted out pages into their respective folders (creation.html in the templates directory will need to be deleted once we 100% know what the form fields will be, and should replace the creation.html file that's currently in the auctions folder.) You can now navigate via the navbar to the login pages, and to get to the item page go to /auctions/1 in the url. - Toby

# 21/10
# Everything is in place for a basic working website once the sql file is created (hopefully it just works) - Toby

# 22/10
# Database is initialised and all basic routings and login systems work. Search functions work. Item creation and page generation works. Landing page should automatically update as you add more listings. Quite a few HTML inconsistencies and weirdness but that's not too pressing right now. - Toby

# 23/10
# A few of the bidding requirements have been fulfilled, namely only the latest bid can be seen and you have to bid higher than the previous bid.

# TO-DO: 
# Everything to do with the watchlist
# Seller is able to determine the starting bid, but cannot bid on the item itself afterwards
# Making only the seller be able to close an auction
# Error handling (probably should be it's own page that you get redirected to for the larger errors like a 404 not found, otherwise a bunch of if statements I suppose)
# Make the site look nice and not a jumbled mess of widgets :)