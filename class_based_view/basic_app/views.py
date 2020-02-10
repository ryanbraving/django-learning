from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models

# Create your views here.


class CBView(View):
    '''it is a very basic class based view
       we don't appreciate how useful CBV is until we use
       generic Template Based View
    '''

    def get(self, request):
        return HttpResponse("Class Based Views are cool!")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "Basic Injection"
        context["school_count"] = models.School.objects.all().count()
        context["student_count"] = models.Student.objects.all().count()
        return context


class SchoolListView(ListView):
    # context_object_name = 'schools'
    # as context, 'school_list' & 'object_list' is getting returened automatically by ListView
    # however we cab changed the context name to be something else e.g. 'schools'
    model = models.School
    # school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    # as context, 'school', & 'object' is getting returened automatically by DetailView
    # however we changed the context name to be 'school_detail'
    model = models.School
    # template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
