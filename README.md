# MediZen Recommendation API

A simple back-end Flask API to serve recommended cannabis strains in the MediZen app
based on desired effects.

- [Usage](#usage)
  - [All Strains](#all-strains)
  - [Recommended Strains](#recommended-strains)
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

    medizen.io/api/strains

---

### Recommended Strains

Endpoint to return a list of recommendations.

    /rec/<n>/<effects>

**Parameters:**

- n: integer - number of recommended strains to return
- effects: string - list of desired effects, comma-delimited (no spaces)

**Returns:** JSON array containing the `id` of top `n` recommendations.

Example:

    medizen.io/api/rec/Uplifted,Happy,Relaxed,Energetic

Returns:

```json
[
    {
        "index": 1629,
        "Strain": "Platinum-Kush"
    },
    {
        "index": 1722,
        "Strain": "Purple-Tangie"
    },
    ...
]
```

---

## Project Information

### Data

[Link to Dataset](https://www.kaggle.com/kingburrito666/cannabis-strains)

The recommendation API uses the Cannabis Strains dataset, uploaded to Kaggle.

We used K-Means Clustering to create 5 categories using the effects and description of
each strain.

Next we pickled a vectorizer and KNN model, which allows the trained model to be
integrated into the Flask app, which also handles the requests, returning the
appropriate JSON data.

---

- [Usage](#usage)
  - [All Strains](#all-strains)
  - [Recommended Strains](#recommended-strains)
- [Project Information](#project-information)
  - [Data](#data)
