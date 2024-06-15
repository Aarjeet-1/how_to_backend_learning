from flask import Blueprint, render_template, request, url_for , flash, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #extracts from init.py
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('emai')
        password = request.form.get('password')
        user = User.query.filter_by(email=email.first())

        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully..',category='success')
                login_user(user, remember=True)
                
            else:
                flash('Incorrect password',category='error')
                return redirect(url_for('views.home'))
    return render_template('login.html', user=current_user)        




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return  redirect(url_for('auth.login'))




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
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')

        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')

        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')   

        elif password1 != password2:
            flash('Password doesn\'t match')
        else:
            new_user = User(email = email, name = name ,password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)


