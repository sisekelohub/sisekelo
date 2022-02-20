from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf.urls.static import static
from Sisekelo import settings
from django.conf import settings
from rest_framework import routers
from courses import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)
from accounts import views as core_views

admin.site.site_header = 'Sisekelo Admin'
admin.site.index_title = 'Sisekelo Management System'

urlpatterns = [
    path('signup/', core_views.signup, name='signup'),
    path("dashboard/", core_views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('application/', include('applications.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('account/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('course-apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        core_views.activate, name='activate'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#test api link http://127.0.0.1:8000/course-apis/courses/

