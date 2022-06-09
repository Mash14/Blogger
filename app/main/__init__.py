from flask import Blueprint
# initialize the blueprint
main = Blueprint('main',__name__)
from . import views,errors