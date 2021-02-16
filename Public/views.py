from django.shortcuts import render
from . import forms
from .models import Profile, Film, Session, Comment
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

def homepage(request):
	return render(request, 'public/homepage.html', {})

def scheme(request):
	return render(request, 'public/scheme.html', {})


def sign_up_view(request):
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['password'] == form.cleaned_data['re_password']:
				user = get_user_model()
				profile = Profile()

				user = user.objects.create_user(form.cleaned_data['login'], password=form.cleaned_data['password'])
				user.save()

				profile.first_name = form.cleaned_data['first_name']
				profile.last_name = form.cleaned_data['last_name']
				profile.email = form.cleaned_data['email']
				profile.user = user
				profile.phone_number = form.cleaned_data['phone']
				profile.save()

				return redirect('/profile/')

	return render(request, 'public/signup.html', {})
