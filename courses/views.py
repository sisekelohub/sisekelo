import secrets
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import *
import mimetypes
import os
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from applications.forms import ApplicationForm
from django.views.generic import ListView
from .models import Learnership, Accredited_Program, Short_Course
from blog.models import Carousel
from rest_framework import viewsets
from rest_framework import permissions
from courses.serializers import CourseSerializer
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from django.urls import reverse


class HomeListView(ListView):
    model = Learnership
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_courses'] = self.model.objects.all().order_by('?')
        return context


def index(request):
    qs = Learnership.objects.all()
    short_courses = Accredited_Program.objects.all()
    images = Carousel.objects.all()[:1]
    jobs = Learnership.objects.all().count()
    company_name = Learnership.objects.all()
    paginator = Paginator(qs, 4)  
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'courses': short_courses,
        'job_qs': jobs,
        'company_name': company_name,
        'image' : images,
        # 'candidates': user
    }
    return render(request, "index.html", context)


def accredited_program(request):
    short_courses = Accredited_Program.objects.all()
    # image = Learnership.objects.get(image)
    # acc_pros =Short_Course.objects.all().count()
    # #user = User.objects.all().count()
    # company_name = Short_Course.objects.all()
    paginate = Paginator(short_courses, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        short_courses = paginate.page(page)
    except PageNotAnInteger:
        short_courses = paginate.page(1)
    except EmptyPage:
        short_courses = paginate.page(paginate.num_pages)

    context = {
        'courses': short_courses,

    }
    return render(request, "index.html", context)


def test(request):
    # queryset = images = Carousel.objects.all()
    queryset = Accredited_Program.objects.all()

    paginate = Paginator(queryset, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        queryset = paginate.page(page)
    except PageNotAnInteger:
        queryset = paginate.page(1)
    except EmptyPage:
        queryset = paginate.page(paginate.num_pages)

    context = {'queryset': queryset}
    return render(request, "course.html", context )


def aprograms(request):
    # queryset = images = Carousel.objects.all()
    queryset = Accredited_Program.objects.all()

    paginate = Paginator(queryset, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        queryset = paginate.page(page)
    except PageNotAnInteger:
        queryset = paginate.page(1)
    except EmptyPage:
        queryset = paginate.page(paginate.num_pages)

    context = {'queryset': queryset}
    return render(request, "courses/aprograms.html", context )

def corporate(request):
    # queryset = images = Carousel.objects.all()
    queryset = Accredited_Program.objects.all()

    paginate = Paginator(queryset, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        queryset = paginate.page(page)
    except PageNotAnInteger:
        queryset = paginate.page(1)
    except EmptyPage:
        queryset = paginate.page(paginate.num_pages)

    context = {'queryset': queryset}
    return render(request, "courses/corporate.html", context )


def learnerships(request):
    # queryset = images = Carousel.objects.all()
    queryset = Accredited_Program.objects.all()

    paginate = Paginator(queryset, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        queryset = paginate.page(page)
    except PageNotAnInteger:
        queryset = paginate.page(1)
    except EmptyPage:
        queryset = paginate.page(paginate.num_pages)

    context = {'queryset': queryset}
    return render(request, "courses/learnerships.html", context )


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Accredited_Program.objects.all().order_by('title')
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CourseDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        course = get_object_or_404(Accredited_Program, slug=slug)
        context = {'course': course}
        return render(request, "courses/course_detail.html", context)

class LearnershipDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        learnership = get_object_or_404(Learnership, slug=slug)
        context = {'learnership':learnership}
        return render(request, "courses/learnership_detail.html", context)