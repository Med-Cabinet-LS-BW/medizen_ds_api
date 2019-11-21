"""
:: MediZen :: Recommendation API ::

A simple back-end Flask API for recommending cannabis strains.
"""

from flask import Flask
import pickle
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()

# api.basilica.ai/embed/text/english
BASILICA = basilica.Connection(config('BASILICA_KEY'))
import BASILICA

app = Flask(__name__)


# Load in the dataset
df = pd.read_csv("data/cannabis.csv")

# Extract index as column
df2 = df.reset_index()

# Load in the pickled vectorizer and knn model
tfidf = pickle.load(open("data/vect_02.pkl", "rb"))
nn = pickle.load(open("data/knn_02.pkl", "rb"))


def recommend(request, n=10):
    """
    Creates a dataframe with top n recommended strains.

    Parameters
    ----------
    request : string
        List of user's desired effects, concatenated into a single string.
        Separated by commas.
    n : int, optional
        Number of recommendations to return, by default 10.

    Returns
    -------
    recs
        Returns a list of recommended strains.
    """

    # Create vector from request string
    # request_vec = tfidf.transform([request])
    # Use Basilica
    request_vec = BASILICA.embed_sentence(request, model='generic')


    # Use knn model to calculate the top n strains
    # The recommendations are the top n nearest points (vectors) to the
    # vectorized request, based on the vectorized dataset (vocab).
    rec_id = nn.kneighbors(request_vec.todense(), n_neighbors=n)[1][0]

    # Convert np.ndarray to pd.Series then to JSON
    rec_json = pd.Series(rec_id).to_json(orient="records")

    return rec_json


# TODO: Determine if `n` should be route parameter
@app.route("/rec/<int:n>/<effects>")
def rec(effects, n=10):
    """
    Primary recommendation route.

    Parameters
    ----------
    n : int, optional
        Number of recommendations to return, by default 10.
    effects : string
        List of desired effects, comma-delimited.

    Returns
    -------
    top : JSON
        Returns a JSON array of top n recommendations.
    """

    try:
        top = recommend(effects, n)
    except Exception as e:
        raise e
        top = "There was an error with the request."

    return str(top)


@app.route("/strains")
def strains():
    """
    Endpoint that returns a list of all available strains.

    Returns
    -------
    strains : JSON
        Returns a JSON array of all available strains.
    """

    try:
        strains = df2.to_json(orient="records")
    except Exception as e:
        raise e
        strains = "There was an error with the request."

    return strains


if __name__ == "__main__":
    app.run()
