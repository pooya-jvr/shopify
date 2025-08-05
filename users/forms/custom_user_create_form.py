from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput,
        error_messages={
            "required": "نام کاربری را وارد کنید.",
            "unique": "این نام کاربری قبلاً ثبت شده است.",
        },
    )

    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput,
        error_messages={
            "required": "ایمیل را وارد کنید.",
            "unique": "این ایمیل قبلاً ثبت شده است.",
        },
    )

    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput,
        error_messages={"required": "رمز عبور را وارد کنید."},
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput,
        error_messages={"required": "تکرار رمز عبور را وارد کنید."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "mobile_number")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "رمز عبور و تکرار آن یکسان نیستند.")

        if password1:
            try:
                validate_password(password1, user=self.instance)
            except ValidationError as e:
                translated_errors = []
                for msg in e.messages:
                    if "too similar" in msg:
                        translated_errors.append(
                            "رمز عبور خیلی شبیه به ایمیل یا نام کاربری است."
                        )
                    elif "too short" in msg:
                        translated_errors.append("رمز عبور خیلی کوتاه است.")
                    elif "too common" in msg:
                        translated_errors.append("رمز عبور خیلی رایج است.")
                    elif "entirely numeric" in msg:
                        translated_errors.append("رمز عبور نباید فقط عدد باشد.")
                    else:
                        translated_errors.append(msg)
                self.add_error("password1", translated_errors)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
