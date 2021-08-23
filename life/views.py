from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import conf
from .models import Configure
from .forms import ContactForm

# Create your views here.

config = Configure.objects.all()

def index(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/?submitted=True")
    else:
        form = ContactForm
        if "submitted" in request.GET:
            submitted = True

    return render(request, "index.html", {"config" : config, "form" : form, "submitted" : submitted })