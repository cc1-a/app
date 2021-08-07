

from webstie.model import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash

auth= Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data= request.form
    
    return render_template('login.html')

@auth.route('/logout')
# def logout():
#     return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        email= request.form.get('email')
        firstName= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email)<4:
            flash("Email must contain 3 or more charachters", category='error')
        elif len(firstName)<2:
            flash("First name cannot be accepted", category='error')
        elif password1==password2:
            flash('Passwords does not mathc', category='error')

        elif len(password1)< 7:
            flash("Password too short", category='error')
        else:
            new_user= User(email=email, fist_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("account created", category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')

