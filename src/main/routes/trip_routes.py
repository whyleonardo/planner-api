from flask import jsonify, Blueprint, request

# Controllers Imports
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder

# Repositories Imports
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

from src.models.settings.db_connection_handler import db_connection_handler


trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_to_invite_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip_by_id(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["PATCH"])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(trip_id)

    return jsonify(response["body"], response["status_code"])


@trips_routes_bp.route("/trips/<trip_id>/create_link", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response["body"], response["status_code"])
