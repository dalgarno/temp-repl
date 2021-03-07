import pytest

from covid_app.validation import validate_input_params


def test_sample_is_required():
    body = {"area_code": "N92000002"}

    with pytest.raises(ValueError) as e:
        validate_input_params(body)

    error_msg = str(e.value)
    assert "Missing required values" in error_msg
    assert "age" in error_msg