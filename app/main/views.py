from sqlalchemy.sql.schema import Index
from ..requests import get_random_quote
from flask import render_template, request, redirect ,url_for ,abort
from . import main
from .. import db, photos
from flask_login import login_required, current_user
from app.models import Post, User,Comment
from .forms import PostForm,CommentsForm, UpdateProfile


@main.route('/')
@main.route('/index')
def index():
    '''
    view root page that returns the view index page and its data
    '''
    quote = get_random_quote()
    posts = Post.get_all_posts()

    return render_template('index.html', quote=quote, posts = posts, current_user = current_user)

@main.route('/new_post/new', methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        user_id = current_user.get_current_object().id
        new_post = Post(user_id=user_id, title=title, description = description)
        new_post.save_post()

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for(main,index))

    return render_template ('new_post.html', form = form )

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Post.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

  
    return render_template("profile/profile.html", user = user, posts= posts)

@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username =name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name=user.username))

    return render_template('profdile/update.html',form =form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

