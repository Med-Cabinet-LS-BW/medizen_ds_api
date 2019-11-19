# MediZen Recommendation

A simple back-end Flask API to recommend cannabis strains in the MediZen app.

- [MediZen Recommendation](#medizen-recommendation)
  - [Usage](#usage)
    - [All Strains](#all-strains)
      - [Example Strains Request](#example-strains-request)
    - [Recommended Strains](#recommended-strains)
      - [Example Recommendation Request](#example-recommendation-request)
  - [Project Information](#project-information)
    - [Data](#data)

## Usage

### All Strains

Endpoint to return a complete list of strains.

    /strains

Parameters: None

Returns: JSON array containing all available strains.

#### Example Strains Request

    medizen.io/api/strains

### Recommended Strains

Endpoint to return a list of recommendations.

    /rec/<effects>

Parameters: Effects: list of desired effects, comma-delimited.

Returns: JSON array of top n recommendations.

#### Example Recommendation Request

    medizen.io/api/rec/Uplifted,Happy,Relaxed,Energetic

---

## Project Information

### Data

[Link to Dataset](https://www.kaggle.com/kingburrito666/cannabis-strains)

The recommendation API uses the Cannabis Strains dataset, uploaded to Kaggle.

We used K-Means Clustering to create 5 categories using the effects and description of
each strain.

Next we pickled a vectorizer and KNN model to create an API that output the top 5 recommendations.
