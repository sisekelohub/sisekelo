from django.urls import path

from . import views
from . views import post_new
urlpatterns = [
	# path('', views.application)
	path('', views.post_new, name='post_new'),

]
