from tabnanny import check
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path  # operating system provides the directory
from flask_login import LoginManager
# from cv2 import face_recognition
import cv2, time


db = SQLAlchemy()
DB_NAME = "faceLogin.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Microsoft engage project'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # initialise database
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    from .views import views
    from .auth import auth
    # from .encodings import encodings

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models
    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where the user will be redirected if they're not logged in yet
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # filter by, ckecks fro primary key id


    
    video = cv2.VideoCapture(0)

    a=1
    while True:
        a= a+1
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Capture', gray)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    print(a)
    video.release()
    cv2.destroyAllWindows()



    #     # Load Camera
    # cap = cv2.VideoCapture(2)
    # while True:
    #     ret, frame = cap.read()
    #      # Detect Faces
    #     face_locations, face_names = sfr.detect_known_faces(frame)
    #     for face_loc, name in zip(face_locations, face_names):
    #         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    #         cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
    #         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    #     cv2.imshow("Frame", frame)
    #     key = cv2.waitKey(1)
    #     if key == 27:
    #         break            
    

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):  # if doesn't already exist, create
        db.create_all(app=app)
        print('Created Database!')
