"""Main app"""

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app, ssl_cert_reqs="CERT_NONE")


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    """Get reviews from Mongo"""
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Search function for reviews"""
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Registration function"""
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in function"""
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """grab the session user's username from db"""
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    """remove user from session cookie"""
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """Add book review function"""
    if request.method == "POST":
        is_liked = "on" if request.form.get("is_liked") else "off"
        review = {
            "genre_name": request.form.get("genre_name"),
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "is_liked": is_liked,
            "review_content": request.form.get("review_content"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genres_name", 1)
    return render_template("add_review.html", genres=genres)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """Edit book review"""
    if request.method == "POST":
        is_liked = "on" if request.form.get("is_liked") else "off"
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "is_liked": is_liked,
            "review_content": request.form.get("review_content"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(reviews_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genres=genres)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """Delete review function"""
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))


@app.route("/get_genres")
def get_genres():
    """Manage genres function"""
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """Add genre function"""
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")

@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    """"Edit category function"""
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    """Delete genre function"""
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_categories"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) ##############################Turn off for submission!!!!!