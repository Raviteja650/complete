from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def sample(request):
    return render(request, 'my_app/full_page.html')

