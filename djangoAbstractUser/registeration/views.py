from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

''' here we import some stuffs we need 
NewUserForm : from the forms file'''

#____________________________ HOME _____________________________________________________

''' the home method  will just render the home.html when accepting request '''

def home(request):
	return render(request=request, template_name='registeration/home.html')

#____________________________ REGISTER _____________________________________________________

''' the register or create account or signup method is responsible  for gitting the new user data making 
sure it valid then add the new user to thee database '''

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("registeration:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registeration/register.html", context={"register_form":form})


#____________________________ LOGIN _____________________________________________________

def login_request(request):


	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("registeration:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registeration/login.html", context={"login_form":form})

#____________________________ LOGOUT _____________________________________________________

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("registeration:home")