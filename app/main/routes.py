from flask import render_template, request, url_for
from app.main import bp
from app.user.controllers import create_user, list_all_users


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
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/admin/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        return list_all_users()
    if request.method == 'POST':
        return create_user()
    else:
        return "Method is Not Allowed"
