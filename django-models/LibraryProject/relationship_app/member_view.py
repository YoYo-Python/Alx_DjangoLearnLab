from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def is_member(user):
    return UserProfile.objects.filter(user=user, role="Member").exists()

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
