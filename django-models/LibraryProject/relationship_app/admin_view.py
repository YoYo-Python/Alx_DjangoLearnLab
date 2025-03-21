from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def is_admin(user):
    return UserProfile.objects.filter(user=user, role="Admin").exists()

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')
