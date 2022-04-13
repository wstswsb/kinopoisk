from flask import Blueprint

blueprint = Blueprint("health_check", __name__)


@blueprint.route("/health_check", methods=["GET"])
def health_check():
    return "healthy", 200
