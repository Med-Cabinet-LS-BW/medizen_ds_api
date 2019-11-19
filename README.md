# MediZen Recommendation API

A simple back-end Flask API to serve recommended cannabis strains in the MediZen app
based on desired effects.

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

    /rec/<n>/<effects>

**Parameters:**

- n: integer - number of recommended strains to return
- effects: string - list of desired effects, comma-delimited (no spaces)

**Returns:** JSON array containing the `id` of top `n` recommendations.

Example:

    https://medizen-ds.herokuapp.com/rec/2/Uplifted,Happy,Relaxed,Energetic

Returns:

```json
[
    {
        "index": 1629,
    },
    {
        "index": 1722,
    },
]
```

### Testing

Flask API is being tested in Advanced Rest Client.

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

- [Usage](#usage)
  - [All Strains](#all-strains)
  - [Recommended Strains](#recommended-strains)
  - [Testing](#testing)
- [Project Information](#project-information)
  - [Data](#data)
