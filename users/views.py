from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def registration(req):
    if req.method == 'POST':
        # fill up form with prev data for reuse in case its not valid
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            # create user, display msg, redirect home
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect('blogTutorial:blog_home')
    else:
        # invalid form, reload page with prefilled form
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})