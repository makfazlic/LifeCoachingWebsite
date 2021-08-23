from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        labels = {
            "name" : "",
            "email" : "",
            "message" : ""
        }
        widgets = {
            "name" : forms.TextInput(attrs={"id" : "name", "type" : "text", "placeholder" : "NAME"}),
            "email" : forms.EmailInput(attrs={"id" : "email", "type" : "text", "placeholder" : "E-MAIL"}),
            "message" : forms.Textarea(attrs={"id" : "message", "type" : "text", "placeholder" : "MESSAGE"})
        }
    
