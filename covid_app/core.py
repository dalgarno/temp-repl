from enum import Enum


class BMI(Enum):
    UNDERWEIGHT = "UNDERWEIGHT"  # bmi <= 18.4
    HEALTHY = "HEALTHY"  # 18.4 < bmi <= 24.9
    OVERWEIGHT = "OVERWEIGHT"  # 25.0 < bmi <= 29.9
    OBESE = "OBESE"  # 30.0 < bmi <= 39.9
    VERY_OBESE = "VERY_OBESE"  # bmi > 40.0


def calculate_bmi(*, height: int, weight: float) -> float:
    return weight / (height / 100) ** 2


def bmi_to_val(bmi: float) -> BMI:
    if bmi < 18.4:
        return BMI.UNDERWEIGHT
    elif bmi < 25:
        return BMI.HEALTHY
    elif bmi < 30:
        return BMI.OVERWEIGHT
    elif bmi < 40:
        return BMI.OBESE
    else:
        return BMI.VERY_OBESE
