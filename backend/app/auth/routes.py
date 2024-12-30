from flask import render_template, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.auth import bp
from app.extensions import db
from app.models.user import User


@bp.route('/')
def index():
    return 'auth.index'


@bp.route('/login', methods=('POST',))
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username != 'test' or password != 'test':
        return jsonify({'msg': 'Bad username or password'}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@bp.route('/register', methods=('POST',))
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    
    if username is None or password is None:
        return jsonify({'msg': 'Username or password is required'}), 400
    
    user = User.query.filter_by(username=username).one()
    if user:
        return jsonify({'msg': 'Username already exists'}), 400
    
    new_user = User(username=username, password=password, email=email)
    db.seesion.add(new_user)
    db.session.commit()
    
    return jsonify({'msg': 'User registered successfully'}), 200



@bp.route('/protected', methods=('GET',))
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
