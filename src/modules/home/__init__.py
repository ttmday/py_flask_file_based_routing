from flask import jsonify, Blueprint

bp = Blueprint("home", __name__)


@bp.route("/")
def home_route():
    return jsonify({"message": "hello world"})
