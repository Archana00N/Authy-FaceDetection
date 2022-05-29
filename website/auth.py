from click import password_option
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # Password hashing for 1st layer of security
from . import db
from flask_login import login_user, login_required, logout_user, current_user # Usermixin can use all info about current user

auth = Blueprint('auth', __name__)

# http request method POST added
@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user: # check password hashing equality
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # log them in, remember till the session is cleared
                import cv2 ,time

                # face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                # smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")

                # video=cv2.VideoCapture(0)

                # while True:
                #     check,frame=video.read()
                #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                #     face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
                #     for x,y,w,h in face:
                #         img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
                #         smile=smile_cascade.detectMultiScale(gray,scaleFactor=1.8,minNeighbors=20)
                #         for x,y,w,h in smile:
                #             img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

                #     cv2.imshow('gotcha',frame)
                #     key=cv2.waitKey(1)

                #     if key==ord('q'):
                #         break

                # video.release()
                # cv2.destroyAllWindows()
            
                                
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required # can't access page if haven't logged in logically
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # collect variables
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        # error handling
        if user: # if user exists,
            flash('Email already exisis', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name)<2:
            flash('Name must be at least 2 characters long.', category='error')
        elif len(password)<7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            # add user to database
            
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user) # user added
            db.session.commit() # commit transaction
            login_user(user, remember=True) # log them in, remember till the session is cleared
            
            flash('Account created!', category='success')
            
            
            
            
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user) # if have access to user, only then show nav bar buttons

