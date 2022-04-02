from flask import Blueprint

seller = Blueprint('seller', __name__, url_prefix='/seller')

from . import routes, models