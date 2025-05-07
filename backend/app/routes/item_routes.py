from flask import Blueprint

item_bp = Blueprint("items", __name__)

@item_bp.route("/test", methods=["GET"])
def test_items():
    return {"message": "Item route working!"}, 200
