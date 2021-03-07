from typing import Any, Dict

import attr


@attr.s(auto_attribs=True, frozen=True)
class InputParams:
    age: str
    height: int
    weight: int
    underlying_health_issues: bool

    def from_dict(d: Dict[str, Any]):
        return InputParams(
            age=d["age"],
            height=d["height"],
            weight=d["weight"],
            underlying_health_issues=d["underlying_health_issues"],
        )


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

    return InputParams.from_dict(data)
