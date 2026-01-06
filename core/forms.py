from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name","email","message"]
        widgets = {
            "name":forms.TextInput(attrs={"placeholder":"Nama Kamu"}),
            "email":forms.EmailInput(attrs={"placeholder":"Email Kamu"}),
            "message":forms.TextInput(attrs={"placeholder":"Pesan Kamu","rows":5}),
        }