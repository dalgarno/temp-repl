from flask import Flask

app = Flask(__name__)

dataset = read_dataset(Path(__file__).parent / "data.json")


@app.route("/compute", methods=["POST"])
def compute():
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
