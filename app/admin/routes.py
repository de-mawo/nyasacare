from flask import Blueprint, render_template, request
from app.user.controllers import create_user, list_all_users

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin():
    return render_template('admin/index.html')


@admin.route('/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        return list_all_users()
    if request.method == 'POST':
        return create_user()
    else:
        return "Method is Not Allowed"
