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

# TO-DO: 
# Defined models.py tables to actually create a database which is needed to store data and display it so we can then make the creation.html page properly as well as login and logout requirements.
# Custom item page that doesn't hard-code it's content.
# Custom watchlist page (this should be similar to a comments section in terms of creating it).
# A way to limit the bid input only being higher than the previous bid
# A way to add to a users personal watchlist
# Making only the seller be able to close an auction
# Close auction?