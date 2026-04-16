from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required



auth_bp = Blueprint("auth", __name__, )

@auth_bp.route("/signup", methods = ["POST"])
def signup():
    data = request.get_json()
    

    if User.query.filter_by(username = data["username"]).first():
        return {"error": "Username already exists"}, 400
    
    hashed = bcrypt.generate_password_hash(data["password"]).decode("utf-8")


    user = User(username=data["username"], email=data["email"], password_hash=hashed)
    db.session.add(user)
    db.session.commit()


    return {"message": "User created successfully"}, 201

@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, data["password"]):
        return {"error": "Invalid credentials"}, 401
    
    token = create_access_token(identity = user.id)
    return {"access_token": token}, 200


@auth_bp.route("/me", methods = ["GET"])
@jwt_required()
def me():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404
    
    return {"username": user.username}, 200



