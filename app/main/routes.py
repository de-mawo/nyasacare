from flask import render_template, request, url_for
from app.main import auth_forms, bp
from app.main.auth_forms import RegistrationForm, LoginForm



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


@bp.route('/')
def index():
    return render_template('index.html', providers=providers)


@bp.route('/login')
def login():
    auth_form = LoginForm()
    return render_template('login.html', title="Login", auth_form=auth_form)


@bp.route('/register')
def register():
    auth_form = RegistrationForm()
    return render_template('register.html', title="Register" , auth_form=auth_form)



