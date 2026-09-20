from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.decorators import (
    login_required
)

from django.contrib import messages

from .models import (
    DonorProfile,
    BloodRequest,
    EmergencyRequest
)

from .forms import (
    RegisterForm,
    DonorForm,
    BloodRequestForm,
    EmergencyForm
)


def home(request):

    donor_count = (
        DonorProfile.objects
        .filter(available=True)
        .count()
    )


    request_count = (
        BloodRequest.objects
        .filter(status="open")
        .count()
    )


    return render(
        request,
        "home.html",
        {
            "donor_count": donor_count,

            "request_count": request_count
        }
    )


def donors(request):

    donors_list = (
        DonorProfile.objects
        .filter(available=True)
        .select_related("user")
    )


    blood_group = request.GET.get(
        "blood_group",
        ""
    )


    city = request.GET.get(
        "city",
        ""
    )


    if blood_group:

        donors_list = donors_list.filter(
            blood_group=blood_group
        )


    if city:

        donors_list = donors_list.filter(
            city__icontains=city
        )


    return render(
        request,
        "donors.html",
        {

            "donors": donors_list[:100],

            "blood_groups": [
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ],

            "bg": blood_group,

            "city": city

        }
    )


def register(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )


        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )


            messages.success(
                request,
                "Account created successfully."
            )


            return redirect(
                "dashboard"
            )

    else:

        form = RegisterForm()


    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )


        password = request.POST.get(
            "password"
        )


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )


            return redirect(
                "dashboard"
            )


        messages.error(
            request,
            "Invalid username or password."
        )


    return render(
        request,
        "login.html"
    )


def logout_view(request):

    logout(request)

    return redirect("home")


@login_required
def dashboard(request):

    profile, created = (
        DonorProfile.objects
        .get_or_create(

            user=request.user,

            defaults={

                "blood_group": "O+",

                "phone": "",

                "city": "",

                "state": "Telangana"

            }
        )
    )


    if request.method == "POST":

        form = DonorForm(
            request.POST,
            instance=profile
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Donor profile updated."
            )


            return redirect(
                "dashboard"
            )

    else:

        form = DonorForm(
            instance=profile
        )


    requests = (
        request.user
        .blood_requests
        .order_by("-created_at")[:5]
    )


    return render(
        request,
        "dashboard.html",
        {

            "form": form,

            "profile": profile,

            "requests": requests

        }
    )


@login_required
def request_blood(request):

    if request.method == "POST":

        form = BloodRequestForm(
            request.POST
        )


        if form.is_valid():

            blood_request = (
                form.save(commit=False)
            )


            blood_request.requester = (
                request.user
            )


            blood_request.save()


            messages.success(
                request,
                "Blood request created."
            )


            return redirect(
                "dashboard"
            )

    else:

        form = BloodRequestForm()


    return render(
        request,
        "request_blood.html",
        {
            "form": form
        }
    )


@login_required
def emergency(request):

    if request.method == "POST":

        form = EmergencyForm(
            request.POST
        )


        if form.is_valid():

            emergency_request = (
                form.save(commit=False)
            )


            emergency_request.requester = (
                request.user
            )


            emergency_request.save()


            messages.success(
                request,
                "Emergency request created."
            )


            return redirect(
                "dashboard"
            )

    else:

        form = EmergencyForm()


    return render(
        request,
        "emergency.html",
        {
            "form": form
        }
    )
