from flask import Blueprint, render_template, request, flash
 
auth = Blueprint('auth', __name__)

# http request method POST added
@auth.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # collect variables
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        
        # error handling
        if len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name)<2:
            flash('Name must be at least 2 characters long.', category='error')
        elif len(password)<7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
            

    return render_template("signup.html")

