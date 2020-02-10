from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from appTwo.models import User
# from . import forms
from appTwo.forms import NewUserForm
# from appTwo.forms import FormName


# Create your views here.

def index(request):
    my_dict = {'insert_me': "this is comming from index view"}
    return render(request, 'appTwo/index.html', context=my_dict)


def image_page(request):
    return render(request, 'appTwo/image-page.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context=user_dict)


def new_user_form_view(request):
    form = NewUserForm()
    if request.method == "POST":  # means if someone has hit the submit button and posted something back
        form = NewUserForm(request.POST)  # then pass in their request

        if form.is_valid():
            form.save(commit=True)  # commit = True to save in DB
            # taking us to the index view which is homepage
            return index(request)
    return render(request, 'appTwo/new_user_form.html', {'myform': form})
