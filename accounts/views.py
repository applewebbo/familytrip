from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from render_block import render_block_to_string

from .forms import ProfileForm
from .models import Profile, TravelFriend


@login_required
def account_profile(request):
    user = request.user
    travel_friends = TravelFriend.objects.filter(user=user).select_related("user__profile")
    context = {
        "user": user,
        "travel_friends": travel_friends,
    }
    if request.htmx:
        html = render_block_to_string("account/profile.html", "profile_info", context)
        response = HttpResponse(html)
        return response
    return render(request, "account/profile.html", context)


@login_required
def profile_edit(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile, pk=user.pk)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": "profileSaved",
                },
            )
        form = ProfileForm(request.POST, instance=profile, pk=user.pk)
        context = {"personal_form": form}
        return render(request, "account/profile_edit.html", context)
    form = ProfileForm(instance=profile, pk=user.pk)
    context = {"personal_form": form}
    return render(request, "account/profile_edit.html", context)
