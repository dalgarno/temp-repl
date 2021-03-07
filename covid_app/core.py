from enum import Enum


class BMI(Enum):
    UNDERWEIGHT = "UNDERWEIGHT"  # bmi <= 18.4
    HEALTHY = "HEALTHY"  # 18.4 < bmi <= 24.9
    OVERWEIGHT = "OVERWEIGHT"  # 25.0 < bmi <= 29.9
    OBESE = "OBESE"  # 30.0 < bmi <= 39.9
    VERY_OBESE = "VERY_OBESE"  # bmi > 40.0


def calculate_bmi(*, height: int, weight: float) -> float:
    return weight / (height / 100) ** 2


def raw_bmi_to_categorical(bmi: float) -> BMI:
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


def case_rate_to_area_modifier(case_rate: float) -> float:
    if case_rate < 9.0:
        return 1.0
    elif case_rate < 49.0:
        return 1.1
    elif case_rate < 99.0:
        return 1.2
    elif case_rate < 199.0:
        return 1.3
    elif case_rate < 399.0:
        return 1.5
    elif case_rate < 799.0:
        return 1.7
    else:
        return 2.0
