from flask import Blueprint

blueprint = Blueprint('analyze', __name__, template_folder='templates')

from . import routes
