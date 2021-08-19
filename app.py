from flask import Flask, request
from pathlib import Path

from covid_app.dataset import read_dataset

app = Flask(__name__)

dataset = read_dataset(Path(__file__).parent / "data.json")

BASELINE_RISK_API = "https://dse-test-api.herokuapp.com"


@app.route("/compute", methods=["POST"])
def compute():
    """
    Estimate the risk factor of an individual to COVID
    based on their health characteristics and area.
    """

    body = request.get_json(force=True)

    # TODO: Finish this method.

    # Note: I've spoken to one of the FE engineers and it wouldn't be a
    # great experience to have our endpoint slow. Can we speed up or do
    # something about the baseline risk API?

    raise NotImplementedError()


@app.route("/areas")
def list_areas():
    """
    List the areas supported by the API.
    """

    return {
        "items": [
            {
                "code": "E12000006",
                "name": "East of England",
            },
            {
                "code": "E12000007",
                "name": "London",
            },
            {
                "code": "E12000003",
                "name": "Yorkshire and The Humber",
            },
            {
                "code": "E12000004",
                "name": "East Midlands",
            },
            {
                "code": "E12000009",
                "name": "South West",
            },
            {
                "code": "E12000001",
                "name": "North East",
            },
            {
                "code": "E12000005",
                "name": "West Midlands",
            },
            {
                "code": "E12000002",
                "name": "North West",
            },
            {
                "code": "E12000008",
                "name": "South East",
            },
        ]
    }
