from django.shortcuts import render, redirect
from .forms import NewAdminForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    """ View function for home page of site. """
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def about(request):
    """ View function for displaying about page of site. """
    context = {}

    return render(request, 'about.html')

def data(request):
    """ View function for displaying data page of site. """
    context = {}

    return render(request, 'data.html')

def contact(request):
    """ View function for displaying contact page of site. """
    context = {}

    return render(request, 'contact.html')

def admin_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def admin_logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:index")

def admin_register(request):
	if request.method == "POST":
		form = NewAdminForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewAdminForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def admin_panel(request):
	""" View function for displaying admin portal page of site. """
	context = {}

	return render(request, 'admin-portal/admin_panel.html')

def contact_support(request):
    """ View function for displaying contact support page of site. """
    context = {}

    return render(request, 'admin-portal/support.html')

def contact_submissions(request):
    """ View function for displaying contact support submissions page of site. """
    context = {}

    return render(request, 'admin-portal/contact_submissions.html')

def dashboard(request):
    """ View function for displaying dashboard page of site. """
    context = {}

    return render(request, 'admin-portal/dashboard.html')

def registered_users(request):
    """ View function for displaying contact support page of site. """
    context = {}

    return render(request, 'admin-portal/registered_users.html')
