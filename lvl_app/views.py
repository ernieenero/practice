from django.shortcuts import render
from lvl_app.forms import UserForm, UserProfileForms
# imports for login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForms(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # one to one relationship
            profile.user = user

            # check
            if 'user_dp' in request.FILES:
                profile.user_dp = request.FILES['user_dp']
            profile.save()

            registered = True
        else:
            print(user_form.error, profile_form.error)
    else:
        user_form = UserForm()
        profile_form = UserProfileForms()

    return render(request, 'basic_app/registration.html',
                                            {'user_form': user_form,
                                            'profile_form': profile_form,
                                            'registered': registered})

@login_required
def special(request):
    return HttpResponse('You are logged in nice')

# this will log in first the user for him to logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        usernames = request.POST.get('username')
        passwords = request.POST.get('password')

        user = authenticate(username=usernames, password=passwords)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account Not Active')
        else:
            return HttpResponse('Invalid Login')
    else:
        return render(request, 'basic_app/login.html', {})
