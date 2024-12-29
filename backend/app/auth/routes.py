from flask import render_template
from app.auth import bp

@bp.route('/')
def index():
    return 'auth.index'
