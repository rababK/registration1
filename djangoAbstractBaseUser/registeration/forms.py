from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your forms here.

class NewUserForm(UserCreationForm):


	class Meta:
		model = User
		fields = ("username", "phone_number", "password1", "password2")
