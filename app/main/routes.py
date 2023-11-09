from flask import redirect, render_template, flash, request, url_for, Blueprint
from flask_login import login_user
from app.main.forms import RegistrationForm, LoginForm
from app.extensions import  bcrypt

from flask import Blueprint
from app.models.user import User

from app.user.controllers import create_user

main = Blueprint('main', __name__)

providers = [
    {
        "name": "Dr. Mathew",
        "speciality": 'Neuorogist',
        "area": "Boston",
        "image": "doc1.jpg"
    },
    {
        "name": "Dr. Johnson",
        "speciality": "Cardiologist",
        "area": "New York",
        "image": "doc2.jpg"
    },

    {
        "name": "Dr. Garcia",
        "speciality": "Pediatrician",
        "area": "Los Angeles",
        "image": "doc3.jpg"
    },

    {
        "name": "Dr. Smith",
        "speciality": "Dermatologist",
        "area": "Chicago",
        "image": "doc4.jpg"
    },

    {
        "name": "Dr. Patel",
        "speciality": "Ophthalmologist",
        "area": "Houston",
        "image": "doc5.jpg"
    },

    {
        "name": "Dr. Williams",
        "speciality": "Orthopedic Surgeon",
        "area": "Philadelphia",
        "image": "doc6.jpg"
    },

    {
        "name": "Dr. Kim",
        "speciality": "ENT Specialist",
        "area": "San Francisco",
        "image": "doc7.jpg"
    },
]


@main.route('/')
def index():
    return render_template('index.html', providers=providers)

@main.route('/provider/<provider>')
def provider(provider):
    return render_template('provider/index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)
 

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        res = create_user(form)
        if res:
            flash('Registration Successful', 'success')
            return redirect(url_for('main.login'))
    else:
        flash('Registration Unsuccessful', 'danger')
    return render_template('register.html', title="Register", form=form)
