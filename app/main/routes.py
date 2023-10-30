from flask import render_template, request
from app.main import bp
from app.user.controllers import create_user, list_all_users 

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/admin/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET': return list_all_users() 
    if request.method == 'POST': return create_user()
    else: return "Method is Not Allowed"
    