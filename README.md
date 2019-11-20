# MediZen Recommendation API

A simple back-end Flask API to serve recommended cannabis strains in the MediZen app
based on desired effects.

- [MediZen Recommendation API](#medizen-recommendation-api)
  - [Usage](#usage)
    - [All Strains](#all-strains)
    - [Recommended Strains](#recommended-strains)
    - [Testing](#testing)
  - [Project Information](#project-information)
    - [Data](#data)

---

## Usage

### All Strains

Endpoint to return a complete list of strains.

    /strains

**Parameters:** None

**Returns:** JSON array containing all available strains.

Example:

    https://medizen-ds.herokuapp.com/strains

---

### Recommended Strains

Endpoint to return a list of recommendations.

    /rec/<n>/<request>

**Parameters:**

- n: integer - number of recommended strains to return
- request: string - list of desired type,effects,flavors
  - comma-delimited, without spaces (see example below)

**Returns:** JSON array containing the `id` of top `n` recommendations.

Example:

    https://medizen-ds.herokuapp.com/rec/5/indica,energetic,talkative,euphoric,creative,focused,orange,tangy,sweet

Returns:

```json
[
    1530,
    2107,
    1156,
    1528,
    2312,
]
```

### Testing

Flask API was tested in Advanced Rest Client and unittests were processed on file app_test.py

---

## Project Information

[Product Vision Document](https://www.notion.so/meds/Product-Vision-3bad180a0bc24c09b27d1b9c4f30c4ba)

[DS initial presentation](https://drive.google.com/file/d/1SWlKu2PWBgG7bUC-hGwdAX8NGLoWuYiA/view?usp=sharing)

### Data

[Link to Dataset](https://www.kaggle.com/kingburrito666/cannabis-strains)

The recommendation API uses the Cannabis Strains dataset, uploaded to Kaggle.

We used K-Means Clustering to create 5 categories using the effects and description of
each strain.

Subsequently, we pickled a vectorizer and KNN model, which allows the trained model to be
integrated into the Flask app and also handles the requests, returning the appropriate JSON data.

---

- [MediZen Recommendation API](#medizen-recommendation-api)
  - [Usage](#usage)
    - [All Strains](#all-strains)
    - [Recommended Strains](#recommended-strains)
    - [Testing](#testing)
  - [Project Information](#project-information)
    - [Data](#data)
