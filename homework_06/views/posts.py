import logging

from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Posts
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/", endpoint="list")
def list_products():
    posts = Posts.query.order_by(Posts.id).all()
    return render_template(
        "posts/list.html",
        posts=posts,
    )


def get_post_name_from_form():
    post_title = request.form.get("post-title")
    if title := (post_title and post_title.strip()):
        return title

    raise BadRequest("field post-title is required!")


def get_post_is_created_from_form():
    created_at = request.form.get("created_at")
    return created_at


def save_post(post_title):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save post {post_title}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save post with name {post_title}!")


@posts_app.route("/<int:post_id>/", methods=["GET", "POST"], endpoint="details")
def get_post_by_id(post_id: int):
    post = Posts.query.get(post_id)
    if post is None:
        raise NotFound(f"Post with id #{post_id} not found!")

    if request.method == "GET":
        return render_template(
            "posts/details.html",
            post=post,
        )

    post_title = get_post_name_from_form()
    if post_title.title == post_title:
        raise BadRequest(f"this product is already named {post_title}")
    if Posts.query.filter_by(title=post_title).count():
        raise BadRequest(f"post with name {post_title!r} already exists!")

    post.title = post_title
    post.created_at = get_post_is_created_from_form()

    save_post(post_title)

    return redirect(url_for("posts_app.details", post_id=post.id))


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    if request.method == "GET":
        return render_template("posts/add.html")

    post_title = get_post_name_from_form()
    created_at = get_post_is_created_from_form()
    post = Posts(title=post_title, created_at=created_at)
    db.session.add(post)
    save_post(post_title)
    return redirect(url_for("posts_app.details", post_id=post.id))
