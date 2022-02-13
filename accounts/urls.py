# from django.conf.urls import url
from django.template.defaulttags import url
from django.urls import path, include

from . import views as core_views, views
from .views import dashboard, signup

app_name = "accounts"


urlpatterns = [
    path("signup/", views.signup, name='signup'),
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    # url(r"^dashboard/", dashboard, name="dashboard"),
    # url(r"^register/", signup, name="register"),
    #
    # url(r'^signup/$', core_views.signup, name='signup'),
    # path("dashboard/", views.dashboard, name='dashboard'),
    path("account_activation_sent/", views.account_activation_sent, name='account_activation_sent'),
    path("activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
        views.activate, name='activate'),

]




# from django.urls import path, include
# # from . import views
# from .views import register, dashboard
# # signup, activate
# # profile, RegisterView

# # from django.conf.urls import url
# from django.urls import re_path as url
# # from . import views

# from accounts import views as user_views, views

# from accounts import views as core_views

# app_name = 'accounts'

# urlpatterns = [
#     # from users.views import dashboard, register


#     url(r"^accounts/", include("django.contrib.auth.urls")),
#     url(r"^dashboard/", dashboard, name="dashboard"),
#     url(r"^register/", register, name="register"),

#     # Add this
#     # path('profile/', profile, name='profile'),
#     # path('profile/', views.ProfileView.as_view(), name='profile'),
#     # path('register/', RegisterView.as_view(), name='register'),
#     # path('register/', user_views.register, name='register'),
#     # path('register/', views.signup, name='register'),
#     # url(r'^signup/$', core_views.signup, name='signup'),
#     # path('profile/', user_views.profile, name='profile'),
#     # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
#     # path('', include('blog.urls')),

#     # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#     # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
#     # url(r'^signup/$', views.signup, name='signup'),
#     # url(r"^dashboard/", core_views.dashboard, name="dashboard"),

    
#     # url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
#     # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     #     views.activate, name='activate'),

# # from users.views import dashboard



# ]

