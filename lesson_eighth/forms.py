from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from lesson_sixth.models import Human

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = [field.name for field in Human._meta.fields]


