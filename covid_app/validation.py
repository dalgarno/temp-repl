from typing import Any, Dict

import attr
import cattr


@attr.s(auto_attribs=True, frozen=True)
class InputParams:
    age_group: str
    height: int
    weight: int
    underlying_health_issues: bool
    area_code: str


def validate_input_params(data: Any) -> InputParams:
    if not isinstance(data, dict):
        raise ValueError("Expected an object")

    missing_fields = []
    for field in attr.fields_dict(InputParams):
        if field not in data:
            missing_fields.append(field)

    if missing_fields:
        formatted_fields = ", ".join(missing_fields)
        raise ValueError(f"Missing required values: {formatted_fields}.")

    return cattr.structure(data, InputParams)
