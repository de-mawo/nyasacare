from flask import render_template
from app.user import bp

@bp.route('/')
def index():
    return render_template('user/index.html')

@bp.route('/history/')
def categories():
    return render_template('user/history.html')