from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import (
    DonorProfile,
    BloodRequest,
    EmergencyRequest
)


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=80
    )


    last_name = forms.CharField(
        max_length=80,
        required=False
    )


    email = forms.EmailField()


    class Meta:

        model = User

        fields = (

            "username",

            "first_name",

            "last_name",

            "email",

            "password1",

            "password2",

        )


class DonorForm(forms.ModelForm):

    class Meta:

        model = DonorProfile

        fields = (

            "blood_group",

            "phone",

            "city",

            "state",

            "available",

        )


class BloodRequestForm(forms.ModelForm):

    class Meta:

        model = BloodRequest

        fields = (

            "patient_name",

            "hospital",

            "blood_group",

            "units",

            "city",

            "phone",

            "urgent",

        )


class EmergencyForm(forms.ModelForm):

    class Meta:

        model = EmergencyRequest

        fields = (

            "patient_name",

            "hospital",

            "blood_group",

            "units",

            "city",

            "phone",

            "details",

        )


        widgets = {

            "details": forms.Textarea(
                attrs={
                    "rows": 4
                }
            )
        }
