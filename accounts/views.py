from django.shortcuts import render


def account_profile(request):
    context = {}
    return render(request, "account/profile.html", context)
