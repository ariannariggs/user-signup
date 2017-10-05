from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

 
 #   If the user's form submission is not valid, you should reject it and 
  #  re-render the form with some feedback to inform the user of what they 
   # did wrong. The following things should trigger an error:

    #The user leaves any of the following fields empty: username, password, 
    #verify password.
   # The user's username or password is not valid -- for example, it contains 
   # a space character or it consists of less than 3 characters or more than 
   # 20 characters (e.g., a username or password of "me" would be invalid).
   # The user's password and password-confirmation do not match.
   # The user provides an email, but it's not a valid email. Note: the email 
   # field may be left empty, but if there is content in it, then it must be validated. 
   # The criteria for a valid email address in this assignment are that it has a single 
   # @, a single ., contains no spaces, and is between 3 and 20 characters long.
   # Each feedback message should be next to the field that it refers to.

   # For the username and email fields, you should preserve what the user typed, so 
   # they don't have to retype it. With the password fields, you should clear them, 
   # for security reasons.

   # If all the input is valid, then you should show the user a welcome page that uses 
   # the username input to display a welcome message of: "Welcome, [username]!"

   # Use templates (one for the index/home page and one for the welcome page) to 
   # render the HTML for your web app.
   # While we've covered how to specify different input types than just text (e.g., 
   # password and email), for this assignment do not use the email input type. 
   # Instead, just use text, which does not do any client-side validation. 
   # This will enable us to check that the server side validation is working by letting
   # errors 
   # through the client side. You should, however, use type='password' for 
   # the password and password verification inputs, to hide the characters typed 
   # (this input type does not include any additional validation).
@app.route("/")
def index():
    return render_template('inputs.html')


@app.route("/", methods=['POST'])
def form_info():
    #pulling infro from the get input template info
    email = request.form["email"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    username = request.form["username"]
   #defining variables
    email_err = ''
    password_err = ''
    verify_password_err = ''
    username_err = ''

    if username == "":
        username_err = 'Your username has to be 3 characters! (But not more than 20.)'
    if password == "":
        password_err = 'Your password has to be 3 characters! (But not more than 20.)'
    if verify_password == "":
        verify_password_err = 'whoops, your passwords are different!'
    #blank stuff

    if len(username) < 3:
        username = ''
        username_err = 'Your username is too tiny! More than 3 characters pls!'
    elif len(username) > 20:
        username = ''
        username_err = 'Woah, too wordy. Fewer than 20 characters pls!'
    else:
        username = username
    #username length error/redirect

    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email = email
        else:
            email = ''
            email_err = 'Your email needs one @ and one . but they should not be at the begining or end!'
    else:
        email = ''
    #email error/redirect

    if len(password) > 20 :
        password = ''
        password_err = 'Keep it between 3 characters and 20 characters pls.'
    elif len(password) < 3:
        password = ''
        password_err = 'Keep it between 3 characters and 20 characters pls.'
    #password length error/redirect

    if password != verify_password:
        password = ''
        verify_password = ''
        verify_password_err = 'Your passwords are not the same, friend!'
    else:
        verify_password = verify_password
    #password matching error/redirect

    if not username_err and not password_err and not verify_password_err and not email_err:
        return render_template('success.html', name = username)
    #they got it!
    else:
        return render_template('inputs.html', email_err=email_err, password_err=password_err, verify_password_err=verify_password_err, username_err=username_err,
        email=email, password=password, verify_password=verify_password,username=username )
    #nope, but give them the chance to try again

app.run()
