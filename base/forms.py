from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # either add list of fields you want to add or just use '__all__' and then exclude the specefic ones.
        fields = '__all__'
        exclude = ['host', 'participants']

class UpdateForm(ModelForm):
    class Meta:
        model = User
        # either add list of fields you want to add or just use '__all__' and then exclude the specefic ones.
        fields = ['avatar', 'name','username', 'email', 'bio']
