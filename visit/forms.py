from django.forms import ModelForm
from .models import Visit


class UserForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'email']