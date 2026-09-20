from django.contrib import admin

from .models import (
    DonorProfile,
    BloodRequest,
    EmergencyRequest
)


@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "blood_group",
        "city",
        "available",
        "verified",
        "donations"
    )


    list_filter = (
        "blood_group",
        "available",
        "verified",
        "state"
    )


    search_fields = (
        "user__username",
        "user__first_name",
        "city",
        "phone"
    )


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):

    list_display = (
        "patient_name",
        "blood_group",
        "hospital",
        "city",
        "units",
        "status",
        "urgent",
        "created_at"
    )


    list_filter = (
        "blood_group",
        "status",
        "urgent",
        "city"
    )


    search_fields = (
        "patient_name",
        "hospital",
        "city"
    )


@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):

    list_display = (
        "patient_name",
        "blood_group",
        "hospital",
        "city",
        "units",
        "active",
        "created_at"
    )


    list_filter = (
        "blood_group",
        "active",
        "city"
    )


    search_fields = (
        "patient_name",
        "hospital",
        "city"
    )
