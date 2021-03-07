import pytest

from covid_app.core import calculate_bmi


@pytest.mark.parametrize(
    "height, weight, expected_bmi", [(180, 80, 24.69), (180, 100, 30.86)]
)
def test_calculate_bmi(height, weight, expected_bmi):
    assert calculate_bmi(height=height, weight=weight) == pytest.approx(
        expected_bmi, abs=1e-2
    )
