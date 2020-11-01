
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG', 'jpeg', 'JPEG'}
Phone_Choices = [("Samsung"), ("Nokia"), ("Apple"), ("Huawei"), ("HTC"), ("Sony"), ("Other")]

class AuctionForm(FlaskForm):
  model = SelectField('Device Make', choices=Phone_Choices)
  name = StringField('Phone Name', validators=[InputRequired('Field is required')])
  #adding two validators, one to ensure input is entered and other to check if the description meets the length requirements
  description = TextAreaField('Description', validators=[InputRequired('Field is required'), Length(min=10, max=1000, message="Description is too short or too long")])
  image = FileField('Item Image', validators=[
                    FileRequired(message='Image cannot be empty'),
                    FileAllowed(ALLOWED_FILE, message='Only supports valid filetypes')])
  starting_bid = IntegerField('Starting Bid (in dollars)', validators=[InputRequired('A starting bid is required')])
  submit1 = SubmitField("Create")
  
class CloseForm(FlaskForm):
    submit2 = SubmitField('Close Listing')

class WatchlistForm(FlaskForm):
    submit3 = SubmitField('Add to Watchlist')
    # not actually being used

class BidForm(FlaskForm):
    bid = IntegerField('Bid (in dollars)', validators=[InputRequired('A bid is required to submit')])
    submit4 = SubmitField('Add Bid')

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("Username", validators=[InputRequired('Enter Username')])
    password=PasswordField("Password", validators=[InputRequired('Enter Password')])
    submit5 = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    phone_number = IntegerField("Phone Number", validators=[InputRequired("Please enter a phone number")])
    address = StringField("Address", validators=[InputRequired("Please enter an address")])
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit6 = SubmitField("Register")