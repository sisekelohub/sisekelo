from django.urls import path

from . import views
from .views import contact

app_name = 'contact'

urlpatterns = [
	
	path('', views.contact, name='contact'),

]