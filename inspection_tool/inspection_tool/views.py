""" 
    The routing for the login functionality of application
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login(request: HttpRequest) -> HttpResponse:
    """
        Summary:
            Default starting page of the inspection tool

        Args:
            request (HttpRequest): a basic http request

        Returns:
            HttpResponse: 
                a classic http response that returns a content
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST.get())
        form.save()
        return render(request, 'layout.html', {'form':form})

    return render(request, 'layout.html')
