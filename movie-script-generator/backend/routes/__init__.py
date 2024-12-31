from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import google_script_routes  # Assuming you will create this file for handling script-related routes.