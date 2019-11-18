"""
:: MediZen :: Recommendation API ::

A simple back-end Flask API for recommending cannabis strains.
"""

from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# db = SQLAlchemy(app)


@app.route("/rec")
def rec():
    """Primary recommendation route."""
    pass
