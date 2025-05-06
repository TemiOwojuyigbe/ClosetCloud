from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/test", methods=["GET"])
def test_auth():
    return {"message": "Auth route working!"}, 200
