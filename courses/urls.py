from django.urls import path
from courses.views import CourseDetailView, LearnershipDetailView, HomeListView, accredited_program, index
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.index),
    path('shortcourses/', views.accredited_program, name='shortcourses'),
    path('courseview/', views.test, name='courseview'),
    path('aprograms/', views.aprograms, name='aprograms'),
    path('corporate/', views.corporate, name='corporate'),
    path('learnerships/', views.learnerships, name='learnerships'),
    path('courses/<slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('learnership/<slug>/', LearnershipDetailView.as_view(), name='learnership_detail'),
    # path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    # path('', HomeListView.as_view(), name='home'),
]



