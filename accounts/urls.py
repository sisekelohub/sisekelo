from django.urls import path

from . import views
from .views import profile, RegisterView 


from accounts import views as user_views

app_name = 'accounts'

urlpatterns = [
    # Add this
    path('profile/', profile, name='profile'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'), 
    # path('register/', user_views.register, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('', include('blog.urls')),

]