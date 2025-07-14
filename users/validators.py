from django.core.exceptions import ValidationError
import re


def validate_mobile_number(value):
    pattern = r"^09\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError("شماره موبایل وارد شده نامعتبر است.")
