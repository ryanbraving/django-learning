from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord
# from django.http import HttpResponse
# Create your views here.


def django_image(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    # render calls the html file from inside templates folder
    return render(request, 'first_app/django_image.html', context=date_dict)


def index(request):
    # render calls the html file from inside templates folder
    return render(request, 'first_app/index.html')


def first_app(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    # render calls the html file from inside templates folder
    return render(request, 'first_app/home.html', context=date_dict)
