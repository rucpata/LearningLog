
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def logout_view(request):
    """Wylogowanie uzytkownika"""
    logout(request)
    return render(request, 'learning_log:index')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')
           

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'users/register.html', context)