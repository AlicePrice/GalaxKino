from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)

	login = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=254)
	phone = forms.CharField(max_length=10)

	password = forms.CharField(widget=forms.PasswordInput)
	re_password = forms.CharField(widget=forms.PasswordInput)

class SignInForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.Form):
	profile = forms.CharField(max_length=32)
	film = forms.CharField(max_length=32)
#	text = forms.TextField()
	rate = forms.IntegerField()


