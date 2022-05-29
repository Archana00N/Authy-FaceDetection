from flask import Blueprint, render_template
from flask_login import login_required, current_user # if not logged in, implement functions of this module
 
views = Blueprint('views', __name__)

@views.route('/')
@login_required # can't access home if haven't logged in
def home():
    return render_template("home.html", user=current_user)