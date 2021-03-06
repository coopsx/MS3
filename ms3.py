from flask import Flask, render_template, url_for, flash, redirect

from forms import LoginForm, RegistrationForm

import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://admin:Redwine@cluster0.pesdg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["LogIn"]
collection = db["Users"]

post = {"_id": 0, "user": "TJ1290",
        "email": "coopsx@googlemail.com", "password": "redREDwhine"}

collection.insert_one(post)

app = Flask(__name__)

app.config['SECRET_KEY'] = '8440dba2fb43df941ec6ad8e8a7f6d56'

posts = [
    {
        'name': 'Tom Jackson',
        'title': 'Introduction',
        'content': 'Introductory Post',
        'date': '26 JUNE, 2021'
    },
    {
        'name': 'James Cooper',
        'title': 'Barolo',
        'content': 'Barolo Wine Review',
        'date': '28 JUNE, 2021'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@wineblog.com' and form.password.data == 'password':
            flash('Login Successful.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Login Unsuccessful. Please check details and try again', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
