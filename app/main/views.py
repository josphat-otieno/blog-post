
from ..request import get_random_quote
from flask import render_template, request, redirect ,url_for ,abort,flash
from . import main
from .. import db, photos
from flask_login import login_required, current_user
from app.models import Post, User,Comment, Subscriber
from .forms import PostForm,CommentsForm, SubscriptionForm, UpdateProfile
from  ..email import mail_message


@main.route('/')
@main.route('/index')
def index():
    '''
    view root page that returns the view index page and its data
    '''
    
    posts = Post.get_all_posts()
    quote = get_random_quote()
    title = 'Bloggers'
    return render_template('index.html', posts = posts, current_user = current_user, quote=quote, title=title)

@main.route('/new_post/new', methods=['GET','POST'])
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        content = post_form.content.data
        user_id = current_user._get_current_object().id
        new_post = Post(user_id=user_id, title=title, content=content)
        new_post.save_post()

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template ('new_post.html', post_form = post_form )

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
def new_Comment(id):
    comment_form = CommentsForm()
    post =Post.query.filter_by(id=id).all()
    comments = Comment.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment=comment_form.comment.data
        name= comment_form.name.data
        new_comment=Comment(comment = comment,name=name, post_id=id)
        new_comment.save_comment()

        db.session.add(new_comment)
        db.session.commit()

    return render_template('comment.html', comment_form=comment_form, comments=comments,post=post)

@main.route('/update_post/<int:id>', methods=['GET', 'POST'])
@login_required
def updatePost(id):
    post = Post.query.get_or_404(id)
    post_form = PostForm()
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.content = post_form.content.data
        user_id = current_user._get_current_object().id
       
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('main.index',user_id=user_id))
    elif request.method == 'GET':
        post_form.title.data = post.title
        post_form.content.data = post.content
       
    return render_template('edit_post.html',post=post, post_form=post_form)

@main.route('/delete_post/<int:id>', methods=['GET', 'POST'])
@login_required
def deletePost(id):
    post = Post.query.get_or_404(id)
    user_id = current_user._get_current_object().id
    db.session.delete(post)
    db.session.commit()
    flash('Blog succesfully deleted')
    return redirect(url_for('main.index',user_id=user_id)) 

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect (url_for('main.new_Comment', id=id)) 

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

@main.route('/subcscribe', methods = ['GET','POST'])
def subscription():
    subscription_form= SubscriptionForm()
    try:
        if subscription_form.validate_on_submit():
            subscriber = Subscriber(email = subscription_form.email.data)
            db.session.add(subscriber)
            db.session.commit()
            flash('Thank you for subscribing to our services, You will recieve daily updates on new blogs')
            mail_message("Welcome to Blogging","email/welcome_user",subscriber.email,subscriber=subscriber)

            return redirect(url_for('main.subscription'))
    except:
        return redirect(url_for('main.index'))

    return render_template ('subscribe.html',  subscription_form = subscription_form)

