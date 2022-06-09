# Where we will create handlers for error pages.
from flask import render_template
from . import main

# app_errorhandler() to use the error handler application wide not only in blueprint
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404