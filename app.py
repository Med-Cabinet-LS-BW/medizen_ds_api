"""
:: med cabinet ::

A Flask API for recommending cannabis strains.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)


@app.route("/rec")
def rec():
    """Primary recommendation route."""
    pass


class Strain(db.Model):
    """A general class to represent a strain."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    strain_type = db.Column(db.String(8), nullable=False)
    avg_rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500))

    # These are all OneHotEncoded (boolean; 1 or 0)
    effect_01 = db.Column(db.Integer, nullable=False)
    effect_02 = db.Column(db.Integer, nullable=False)
    effect_03 = db.Column(db.Integer, nullable=False)
    effect_04 = db.Column(db.Integer, nullable=False)
    effect_05 = db.Column(db.Integer, nullable=False)
    effect_06 = db.Column(db.Integer, nullable=False)
    effect_07 = db.Column(db.Integer, nullable=False)
    effect_08 = db.Column(db.Integer, nullable=False)
    effect_09 = db.Column(db.Integer, nullable=False)
    effect_10 = db.Column(db.Integer, nullable=False)

    # These are all OneHotEncoded (boolean; 1 or 0)
    flavor_01 = db.Column(db.Integer, nullable=False)
    flavor_02 = db.Column(db.Integer, nullable=False)
    flavor_03 = db.Column(db.Integer, nullable=False)
    flavor_04 = db.Column(db.Integer, nullable=False)
    flavor_05 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Exp '{self.name}'>"


class User(db.Model):
    """A general class to represent a user."""

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Exp '{self.name}'>"


class Experience(db.Model):
    """A general class to represent a user's experience."""

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id") nullable=False)
    user = db.relationship("User", backref=db.backref("experiences", lazy=True))

    strain_id = db.Column(db.Integer, db.ForeignKey("strain.id") nullable=False)
    strain = db.relationship("Strain", backref=db.backref("strains", lazy=True))

    def __repr__(self):
        return f"<Exp '{self.user}'>"
