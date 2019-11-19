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

app = Flask(__name__)


# Load in the dataset
df = pd.read_csv("data/cannabis.csv")

# Extract index as column
df2 = df.reset_index()

# Load in the pickles
tfidf = pickle.load(open("data/vect_01.pkl", "rb"))
nn = pickle.load(open("data/knn_01.pkl", "rb"))


def recommend(request, n=5):
    """
    Creates a dataframe with top n recommended strains.
    
    Parameters
    ----------
    request : string
        List of user's desired effects, concatenated into a single string.
        Separated by commas.
    n : int, optional
        Number of recommendations to return, by default 5
    
    Returns
    -------
    recs
        Returns a list of recommended strains.
    """

    # Transform
    request = pd.Series(request)
    request_sparse = tfidf.transform(request)

    # Send to df
    request_tfidf = pd.DataFrame(request_sparse.todense())

    # Return a list of indexes
    top5 = nn.kneighbors([request_tfidf][0], n_neighbors=5)[1][0].tolist()
    
    # Send recomendations to DataFrame
    recs_df = df.iloc[top5].reset_index()

    # Extract pd.Series of only "Strain"
    recs_dict = recs_df[["index", "Strain"]].to_json(orient="records")
    
    return recs_dict

# TODO: Determine if `n` should be route parameter
@app.route("/rec/<effects>")
def rec(effects):
    """
    Primary recommendation route.
    
    Parameters
    ----------
    effects : string
        List of desired effects, comma-delimited.

    Returns
    -------
    top : JSON
        Returns a JSON array of top n recommendations.
    """

    try:
        top = recommend(effects)
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
        # TODO: Return index+name or just index
        strains = df2[["index", "Strain"]].to_json(orient="records")
    except Exception as e:
        raise e
        strains = "There was an error with the request."

    return strains

