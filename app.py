from flask import Flask, render_template, redirect, url_for, request, session,flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User, JobPreference
import os

from main_scraper import build_internshala_url, scrape_jobs_to_csv,send_email_with_csv


app = Flask(__name__)
app.secret_key = 'secret-key' 

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'internshala.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)


@app.route('/')
def home():
    return render_template("home.html")

from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("⚠️ Email already taken! Please use a different one.", "danger")
            return redirect(url_for('register'))

      
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        
        user = User.query.filter_by(email=email).first()
        if user:
            session['user_id'] = user.id  
            return redirect(url_for('preferences'))
        else:
            return "User not found."
    return render_template('login.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = User.query.get(user_id)

    if request.method == 'POST':
        keyword = request.form['keyword']
        location = request.form['location']

       
        existing_pref = JobPreference.query.filter_by(user_id=user_id).first()
        if existing_pref:
            existing_pref.keyword = keyword
            existing_pref.location = location
        else:
            new_pref = JobPreference(keyword=keyword, location=location, user_id=user_id)
            db.session.add(new_pref)

        db.session.commit()

        
        try:
            url = build_internshala_url(keyword, location)
            filename = f"{user.username}_jobs.csv"
            scrape_jobs_to_csv(url, filename)
            send_email_with_csv(user.email, user.username, filename)
            flash(f"Success! Jobs sent to {user.email}")
        except Exception as e:
            print(f" Error sending email: {e}")
            flash("An error occurred while sending your job list.")

    return render_template('preferences.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
