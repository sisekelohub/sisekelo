from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
 
  