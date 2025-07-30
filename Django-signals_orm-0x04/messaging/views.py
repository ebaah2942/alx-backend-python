from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

# Create your views here.

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out before deleting
        user.delete()
        return redirect('account_deleted')  # Replace with your URL or success message
    return HttpResponseForbidden("You can't access this directly.")

