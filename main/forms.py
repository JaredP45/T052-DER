from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewAdminForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewAdminForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ContactForm(ModelForm):
	# TODO: save contact details
	email = forms.EmailField(required=True)

	class Meta:
		model = Contact
		fields = ("full_name", "email", "phone_number", "subject", "message")

	def save(self, commit=True):
		contact = super(ContactForm, self).save(commit=False)
		contact.email = self.cleaned_data['email']
		if commit:
			contact.save()
		return contact


class ContactSupportForm(forms.Form):
	username = forms.CharField(max_length=50)
	email_address = forms.EmailField(max_length=150)
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea, max_length=2000)
