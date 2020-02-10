from django.urls import path
from appTwo import views

urlpatterns = [
    # path('', views.index, name = "index")
    path('', views.new_user_form_view, name = "form")
]
