# COVID-19 Risk Factor Estimator 🦠

## Overview

The app estimates the current "risk factor" (a positive floating point number >= 1.0) of an individual in England regarding COVID-19. The value computed will be used in downstream services.

The risk factor comprises two elements:

- a baseline risk
- an area modifier

These are multiplied together to get the final value.

For reference:

```
risk_factor = baseline_risk * area_modifier
```

Note: the risk factor it produces is "for example only", and does not consitute medical advice!

### Baseline risk

This value is calculated by a separate service which serves an ML classifier model. The service's API is documented [here](https://dse-test-api.herokuapp.com).

Based on BMI, underlying health issues, and age it predicts a risk category from 1 (lowest risk) to 10 (highest risk).

The API's response for a `200 SUCCESS` is like:

```JSON
{
  "risk_category": 4
}
```

The service's performance is variable, and the underlying model will not be changing as the team responsible is migrating to a new service.

### Area modifier

The dataset in `data.json` contains the rate of new cases for the current week (assuming the current week is the first week in March!) for each region in England
[published by the UK government](https://coronavirus.data.gov.uk/).

```javascript
{
    "length": 9,
    "body": [
      {
        "date": "2021-03-01",
        "areaType": "region",
        "areaCode": "E12000006",
        "areaName": "East of England",
        "newCasesBySpecimenDateRollingRate": 61.3
      },
      // etc
    ]
}
```

There is a function provided (`case_rate_to_area_modifier`) which converts the case rate to a modifier.

---

## Goals 🎯

As you will discover, the app is not ready for production quite yet! The goals are:

1. Talk through the code and explain what it does.
2. Run the application, and make a request with `curl`.
3. Implement the `/compute` endpoint. With tests!

Don't worry if the endpoint is not completed by the end of the interview. Points of discussion during the interview will affect how much code ends up being written.

## App overview

The API exposes three endpoints:

- `GET /health` - returns the health of the service.
- `GET /areas` - returns a list of regions in England.
- `POST /compute` - given an individual's health characteristics and area, returns a risk factor with regards to COVID-19.

The available regions are returned by the `GET /areas` API:

```bash
curl http://localhost:5000/areas
```

```json
{
  "items": [
    {
      "code": "E12000006",
      "name": "East of England"
    },
    {
      "code": "E12000007",
      "name": "London"
    },
    {
      "code": "E12000003",
      "name": "Yorkshire and The Humber"
    }
    // etc
  ]
}
```

And a caller uses the `POST /compute` API to calculate the risk factor:

```bash
 curl -X POST localhost:5000/compute --data '{"height": 180, "weight": 75, "underlying_health_issues": false, "age_group": "group_1", "area_code": "E12000007"}'
```

Due to the need to keep as much data anonymised as possible, we deal in `age_groups` rather than specific ages.

| Age range | Group id |
| --------- | -------- |
| < 18      | group_0  |
| (18, 30]  | group_1  |
| (30, 45]  | group_2  |
| (45, 65]  | group_3  |
| (65, 80]  | group_4  |
| > 80      | group_5  |

## Application structure 🔭

The app is written in Python using the Flask framework.

```
covid_app/
  core.py        ← module to compute the risk factor
  dataset.py     ← module to read the dataset from the filesystem
  validation.py  ← module to validate incoming requests

tests/           ← unit tests

app.py           ← API views
data.json        ← rate of new cases per region
requirements.txt ← Python dependencies
```

## Running the app

### Locally

The app should run on Python3.7+. Feel free to set up as you feel comfortable, but for reference you can:

1. Create a virtualenv and install the requirements:

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip3 install -r requirements.txt
```

2. Run the app:

```bash
$ flask run
```

3. Run the tests:

```bash
$ pytest tests
```

### Repl.it

We also provide the ability to run the app in an online IDE, called [repl.it](https://replit.com/).

You can simply click the green _Run_ button to run the app and the output will be shown in the _Console_ tab.

You can run commands from the _Shell_ tab for example:

```bash
$ curl localhost:5000/
```

```bash
$ pytest tests
```

You have access to a key value store with a similar API to that of a Python dictionary:

```Python
from replit import db

db["key"] = "value"
```
