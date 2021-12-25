from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import PlutoUser


class PlutoUserCreationForm(UserCreationForm):
    class Meta:
        model = PlutoUser
        fields = ('email',)


class PlutoUserChangeForm(UserChangeForm):
    class Meta:
        model = PlutoUser
        fields = ('email',)
