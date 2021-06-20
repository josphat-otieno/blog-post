from ..requests import get_random_quote
from flask import render_template, request, redirect ,url_for ,abort
from . import main

@main.route('/')
def index():
    '''
    view root page that returns the view index page and its data
    '''
    quote = get_random_quote()

    return render_template('index.html', quote=quote)