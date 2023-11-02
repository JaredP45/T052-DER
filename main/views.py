from django.shortcuts import render, redirect
from .forms import NewAdminForm, ContactForm, ContactSupportForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm, ContactSupportForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import ContactSupport
from django.contrib.auth.models import User

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
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = f"Inquiry: {form.cleaned_data.get('subject')}"
			# body = {
			# 	'full_name': form.cleaned_data.get('full_name'), 
			# 	'email': form.cleaned_data.get('email_address'), 
			# 	'phone_number': form.cleaned_data.get('phone_number'), 
			# 	'message': form.cleaned_data.get('message')
			# }
			# message = "\n".join(body.values())
			
			# FIXME: message not able to be parsed
			message="Message body"
			try:
				messages.success(request, "Email successfully sent!")
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
				
			except BadHeaderError:
				messages.error(request, "Unable to send email. Please try again later.")
			return redirect ("main:index")
	form = ContactForm()
	return render(request, "contact.html", {'contact_form':form})

def contact_support(request):
	# TODO: Implement changes similiar in contact
	if request.method == 'POST':
		form = ContactSupportForm(request.POST)
		if form.is_valid():
			form.save()
			subject = f"Support: {form.cleaned_data.get('subject')}"
			# body = {
			# 	'username': form.cleaned_data.get('username'), 
			# 	'email': form.cleaned_data.get('email_address'),
			# 	'message': form.cleaned_data.get('message')
			# }
			# message = "\n".join(body.values())
			
			# FIXME: message not able to be parsed
			message="Message body"
			try:
				messages.success(request, "Email successfully sent!")
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				messages.error(request, "Unable to send email. Please try again later.")
			return redirect("main:contact_submissions")
      
	form = ContactSupportForm()
	return render(request, "admin-portal/support.html", {'contact_support_form': form})

def contact_submissions(request):
	submissions = ContactSupport.objects.all()
	return render(request, 'admin-portal/contact_submissions.html', {'submissions': submissions})

def admin_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Welcome, {username}!")
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

def dashboard(request):
    """ View function for displaying dashboard page of site. """
    context = {}

    return render(request, 'admin-portal/dashboard.html')

def registered_users(request):
	""" View function for displaying contact support page of site. """
	users = User.objects.all().values()
	return render(request, 'admin-portal/registered_users.html', {'users': users})

"""
TODO:
	Some pages are accessible without authentication (contact submissions, dashboard, registered users) due to the pages being connected to admin panel.
	These pages should be rendered as templates within Django views in order for authentication to work properly.
"""
