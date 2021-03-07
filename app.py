from flask import Flask, request
from pathlib import Path

from covid_app.dataset import read_dataset
from covid_app.validation import validate_input_params

app = Flask(__name__)

dataset = read_dataset(Path(__file__).parent / "data.json")


@app.route("/compute", methods=["POST"])
def compute():

    body = request.get_json(force=True)

    try:
        input_params = validate_input_params(body)
    except ValueError as exc:
        return {"message": str(exc)}, 400

    breakpoint()

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

@app.route("/health")
def health():
    return {"status": "healthy"}
