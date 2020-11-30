from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
    if req.method == 'POST':
        u_form = UserUpdateForm(req.POST, instance=req.user)
        p_form = ProfileUpdateForm(req.POST,
                                   req.FILES,
                                   instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(req, f'Your profile has been updated!')
            # must redirect instead of falling to render below
            #    to avoid resubmit error msg in browser
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(req, 'users/profile.html', context)
