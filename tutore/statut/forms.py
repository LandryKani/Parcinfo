from django.forms import ModelForm

from statut.models import Statut


class StatutForm(ModelForm):
    class Meta:
        model = Statut
        fields = '__all__'
