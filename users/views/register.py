from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm

import json


def register(request):
    if request.method == "POST":

        data = json.loads(request.body)

        form = CustomUserCreationForm(data)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
