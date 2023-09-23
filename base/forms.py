from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # either add list of fields you want to add or just use '__all__' and then exclude the specefic ones.
        fields = '__all__'
        exclude = ['host', 'participants']