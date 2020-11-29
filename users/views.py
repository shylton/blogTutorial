from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def registration(req):
    if req.method == 'POST':
        # fill up form with prev data for reuse in case its not valid
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            # create user, display msg, redirect home
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!'
                                  f'Please log in.')
            return redirect('login')
    else:
        # invalid form, reload page with prefilled form
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})


@login_required
def profile(req):
    return render(req, 'users/profile.html')
