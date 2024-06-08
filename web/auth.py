from flask import Blueprint, render_template, request, url_for ,flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    
    return render_template("login.html", boolean=True)



@auth.route('/logout')
def logout():
    return  "you've been  logged out!!"
@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()

        if user :
            flash('Email already exists.',category='error')
        elif password1 != password2:
            flash('Password doesn\'t match')
        else:
            new_user = User(email = email, name = name ,password = generate_password_hash(password1, method='sha256'))

    return render_template("sign-up.html")


