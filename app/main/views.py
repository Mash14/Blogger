from datetime import datetime
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Upvote,Downvote
from .forms import UpdateProfileForm,CreateBlogForm,CreateCommentForm
from ..request import get_quotes
import markdown2


# create views
@main.route('/')
def index():
    '''
    View root page function that 
    returns the index page and its data
    '''
    blogs = Blog.query.order_by(Blog.post_time.desc()).all()
    quote = get_quotes()
    
    title = 'Blogger'
    return render_template('index.html',blogs = blogs,title = title,quote = quote)


@main.route('/profile/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user = current_user).order_by(Blog.post_time.desc()).all()

    if user is None:
        abort(404)

    # format_bio = markdown2.markdown(user.bio,extras = ["code-friendly","fenced-code-blocks"])
    title = f'{user.username}\'s profile'

    return render_template('profile/profile.html',title = title,user = user,blogs = blogs)


@main.route('/update/profile/<uname>/bio' ,methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfileForm()

    if form.validate_on_submit():
        user.bio = form.bio.data 

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    title = f'{user.username} bio update'
    return render_template('profile/update_profile.html',title = title, form = form)


@main.route('/change/update/profile/<uname>/bio' ,methods = ['GET','POST'])
@login_required
def change_bio(uname):
    user = User.query.filter_by(username = uname).first()
    if user != current_user:
        abort(403)

    form = UpdateProfileForm()

    if form.validate_on_submit():
        user.bio = form.bio.data 

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname = uname))

    elif request.method == 'GET':
        form.bio.data = user.bio

    title = f'{user.username} Bio Update'
    return render_template('profile/update_profile.html',form = form,title = title)


@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path 
        db.session.commit()

    return redirect(url_for('main.profile',uname = uname))


@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def create_blog():

    form = CreateBlogForm()

    if form.validate_on_submit():
        title = form.title.data 
        post = form.post.data 
        category = form.category.data 

        new_blog = Blog(title = title,post = post,category = category, post_time = datetime.now(),user = current_user)
        new_blog.save_blog()

        return redirect(url_for('.single_blog',blog_id = new_blog.id))

    title = 'New Blog'
    return render_template('new_blog.html',title = title, form = form)


@main.route('/update/blog/<int:blog_id>')
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        abort(404)
    if blog.user != current_user:
        abort(403)

    form = CreateBlogForm()

    if form.validate_on_submit():
        blog.title = form.title.data 
        blog.post = form.post.data 
        blog.category = form.category.data 
        blog.post_time = datetime.now()

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.single_blog',blog_id = blog.id))

    elif request.method == 'GET':
        form.title.data = blog.title
        form.post.data = blog.post
        form.category.data = blog.category

    title = f'{blog.title} update'
    return render_template('update_blog.html',title = title,blog = blog,form = form)


@main.route('/blog/<int:blog_id>', methods = ['GET','POST'])
@login_required
def single_blog(blog_id):
    comments = Comment.query.filter_by(blog_id = blog_id).order_by(Comment.time.desc()).all()

    blog = Blog.query.get(blog_id)
    form = CreateCommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment = comment,time = datetime.now(),user = current_user,blog_id = blog_id)
        new_comment.save_comment()

        return redirect(url_for('main.single_blog',blog_id = blog_id))
    format_post = markdown2.markdown(blog.post,extras = ["code-friendly","fenced-code-blocks"])
    # format_comment = markdown2.markdown(comments.comment,extras = ["code-friendly","fenced-code-blocks"])
    title = f'{blog.title}'
    return render_template('single_blog.html',title = title,form = form,comments = comments,blog = blog,format_post = format_post)


@main.route('/blog/category/<category>')
def category(category):
    blogs = Blog.query.filter_by(category = category).all()

    title = f'{category}'
    return render_template('category.html',blogs = blogs,title = title)


@main.route('/delete/blog/<int:blog_id>', methods = ['GET','POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.index'))


@main.route('/delete/comment/<int:comment_id>',methods = ['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('.single_blog',blog_id = comment.blog_id))


@main.route('/blog/like/<int:blog_id>', methods = ['GET','POST'])
@login_required
def like_blog(blog_id):
    upvotes = Upvote.get_upvotes(blog_id)
    # one user one vote
    person_vote = f'{current_user.id}:{blog_id}'
    for upvote in upvotes:
        single_vote = f'{upvote}'
        if person_vote == single_vote:
            return redirect(url_for('main.index'))
        else:
            continue 

    new_vote = Upvote(user = current_user,blog_id = blog_id)
    new_vote.save_upvote()
    return redirect(url_for('main.index',blog_id = blog_id))


@main.route('/blog/dislike/<int:blog_id>',methods = ['GET','POST'])
@login_required
def dislike_blog(blog_id):
    downvotes = Downvote.get_downvotes(blog_id)
    # one user one vote
    person_vote = f'{current_user.id}:{blog_id}'
    for downvote in downvotes:
        single_vote = f'{downvote}'
        if person_vote == single_vote:
            return redirect(url_for('main.index'))
        else:
            continue 
    new_downvote = Downvote(user = current_user,blog_id = blog_id)
    new_downvote.save_downote()
    return redirect(url_for('main.index',blog_id = blog_id))  