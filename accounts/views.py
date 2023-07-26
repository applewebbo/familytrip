from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

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
    return render(request, "account/profile.html", context)


@login_required
def profile_edit(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        form = ProfileForm(request.POST, instance=profile)
        context = {"personal_form": form}
        return render(request, "account/profile_edit.html", context)
    form = ProfileForm(instance=profile)
    context = {"personal_form": form}
    return render(request, "account/profile_edit.html", context)
