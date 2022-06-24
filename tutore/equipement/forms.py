from django.forms import ModelForm
from equipement.models import Equipement


class EquipementForm(ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'
