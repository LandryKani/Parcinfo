from django.forms import ModelForm
from categorie.models import Categorie


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
