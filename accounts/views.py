from django.shortcuts import get_object_or_404, render

from .models import CustomUser, TravelFriend


def account_profile(request):
    user = get_object_or_404(CustomUser, email=request.user)
    travel_friends = TravelFriend.objects.filter(user=user)
    context = {
        "user": user,
        "travel_friends": travel_friends,
    }
    return render(request, "account/profile.html", context)
