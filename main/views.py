from django.shortcuts import render

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

def login(request):
    """ View function for displaying login page of site. """
    context = {}

    return render(request, 'login.html')
