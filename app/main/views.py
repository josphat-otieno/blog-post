from ..requests import get_random_quote
from flask import render_template, request, redirect ,url_for ,abort
from . import main
from flask_login import login_required, current_user
from app.models import Post, User,Comment


@main.route('/')
@main.route('/index')
def index():
    '''
    view root page that returns the view index page and its data
    '''
    quotes = get_random_quote()
    posts = Post.query.all()

    return render_template('index.html', quotes=quotes, posts = posts, current_user = current_user)