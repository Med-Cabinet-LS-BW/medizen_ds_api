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
  - [Deployment](#deployment)

---

## Usage

### All Strains

Endpoint to return a complete list of strains.

    /strains

**Parameters:** None

**Returns:** JSON array containing all available strains.

Example:
` https://medizen-ds.herokuapp.com/strains`

Returns:

    `[{"index":0,"Strain":"100-Og","Type":"hybrid","Rating":4.0,"Effects":"Creative,Energetic,Tingly,Euphoric,Relaxed","Flavor":"Earthy,Sweet,Citrus","Description":"$100 OG is a 50\/50 hybrid strain that packs a strong punch. The name supposedly refers to both its strength and high price when it first started showing up in Hollywood. As a plant, $100 OG tends to produce large dark green buds with few stems. Users report a strong body effect of an indica for pain relief with the more alert, cerebral feeling thanks to its sativa side."},{"index":1,"Strain":"98-White-Widow","Type":"hybrid","Rating":4.7,"Effects":"Relaxed,Aroused,Creative,Happy,Energetic","Flavor":"Flowery,Violet,Diesel","Description":"The \u201898 Aloha White Widow is an especially potent cut of White Widow that has grown in renown alongside Hawaiian legends like Maui Wowie and Kona Gold. This White Widow phenotype reeks of diesel and skunk and has a rich earthy taste with intermittent notes of hash. Its buds are coated in trichomes, giving its dark foliage a lustrous glint to go along with its room-filling odor. This one-hitter-quitter uplifts the mind with mind-bending euphoria that materializes in the body as airy relaxation. \u201898 Aloha White Widow is available from Pua Mana 1st Hawaiian Pakal\u014dl\u014d Seed Bank. \u00a0"},...`

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

    https://medizen-ds.herokuapp.com/rec/5/sativa,energetic,talkative,euphoric,creative,focused,orange,tangy,sweet

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

## Deployment

Find the last version of the Flask API on:

[Strains](https://medizen-ds.herokuapp.com/strains)
[Recommendations example](https://medizen-ds.herokuapp.com/rec/5/indica,energetic,talkative,euphoric,creative,focused,orange,tangy,sweet)

---

- [MediZen Recommendation API](#medizen-recommendation-api)
  - [Usage](#usage)
    - [All Strains](#all-strains)
    - [Recommended Strains](#recommended-strains)
    - [Testing](#testing)
  - [Project Information](#project-information)
    - [Data](#data)
  - [Deployment](#deployment)
