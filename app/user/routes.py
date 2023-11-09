from flask import Blueprint, render_template


user = Blueprint('user', __name__)


@user.route('/')
def index():
    return render_template('user/index.html')

@user.route('/history/')
def categories():
    return render_template('user/history.html')