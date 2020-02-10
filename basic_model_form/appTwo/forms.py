from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()

    class Meta():  #we can just use Meta without parentheses
        model = User
        fields = '__all__'


