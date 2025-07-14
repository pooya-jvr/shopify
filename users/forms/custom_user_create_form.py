from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "mobile_number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].error_messages = {
            "required": "نام کاربری الزامی است.",
            "unique": "این نام کاربری قبلاً استفاده شده است.",
        }

        self.fields["email"].error_messages = {
            "required": "ایمیل الزامی است.",
            "invalid": "فرمت ایمیل معتبر نیست.",
            "unique": "این ایمیل قبلاً استفاده شده است.",
        }

        self.fields["mobile_number"].error_messages = {
            "required": "شماره موبایل الزامی است.",
            "invalid": "فرمت شماره موبایل درست نیست.",
            "unique": "این شماره موبایل قبلاً ثبت شده است.",
        }

        self.fields["password1"].error_messages = {
            "required": "رمز عبور را وارد کنید.",
        }

        self.fields["password2"].error_messages = {
            "required": "تکرار رمز عبور را وارد کنید.",
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبور و تکرار آن یکسان نیستند.")

        return cleaned_data
