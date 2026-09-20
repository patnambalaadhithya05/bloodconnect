from django.db import models

from django.contrib.auth.models import User


class DonorProfile(models.Model):

    BLOOD_GROUPS = [

        ("A+", "A+"),

        ("A-", "A-"),

        ("B+", "B+"),

        ("B-", "B-"),

        ("AB+", "AB+"),

        ("AB-", "AB-"),

        ("O+", "O+"),

        ("O-", "O-"),

    ]


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS
    )


    phone = models.CharField(
        max_length=20
    )


    city = models.CharField(
        max_length=80
    )


    state = models.CharField(
        max_length=80,
        default="Telangana"
    )


    available = models.BooleanField(
        default=True
    )


    verified = models.BooleanField(
        default=False
    )


    donations = models.PositiveIntegerField(
        default=0
    )


    last_donation = models.DateField(
        null=True,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        name = (
            self.user.get_full_name()
            or self.user.username
        )

        return f"{name} - {self.blood_group}"


class BloodRequest(models.Model):

    STATUS = [

        ("open", "Open"),

        ("matched", "Donor Contacted"),

        ("fulfilled", "Fulfilled"),

        ("cancelled", "Cancelled"),

    ]


    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blood_requests"
    )


    patient_name = models.CharField(
        max_length=120
    )


    hospital = models.CharField(
        max_length=160
    )


    blood_group = models.CharField(
        max_length=3
    )


    units = models.PositiveIntegerField(
        default=1
    )


    city = models.CharField(
        max_length=80
    )


    phone = models.CharField(
        max_length=20
    )


    urgent = models.BooleanField(
        default=False
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="open"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"{self.patient_name} - "
            f"{self.blood_group}"
        )


class EmergencyRequest(models.Model):

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    patient_name = models.CharField(
        max_length=120
    )


    hospital = models.CharField(
        max_length=160
    )


    blood_group = models.CharField(
        max_length=3
    )


    units = models.PositiveIntegerField(
        default=1
    )


    city = models.CharField(
        max_length=80
    )


    phone = models.CharField(
        max_length=20
    )


    details = models.TextField(
        blank=True
    )


    active = models.BooleanField(
        default=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"Emergency - "
            f"{self.patient_name}"
        )
