from flask import Blueprint, render_template
from flask_login import login_required


user = Blueprint('user', __name__)


@user.route('/')
@login_required
def index():
    return render_template('user/index.html', title='User')

@user.route('/history')
@login_required
def categories():
    return render_template('user/history.html')