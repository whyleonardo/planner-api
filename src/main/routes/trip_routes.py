from flask import jsonify, Blueprint

trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    """
    create a data trip
    """

    return jsonify({"message": "Hello World"}), 200
