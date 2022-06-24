from django.forms import ModelForm
from panne.models import Panne


class PanneForm(ModelForm):
    class Meta:
        model = Panne
        fields = '__all__'