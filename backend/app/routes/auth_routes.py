from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db, bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check if the email or username already exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email) 
    ).first()

    if existing_user:
        return jsonify({"error": "Username or email already exists."}), 400
    
    # Hash the password
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    # Create a new user instance
    new_user = User(username=username, email=email, password_hash=password_hash)

    # Add and commit to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201
