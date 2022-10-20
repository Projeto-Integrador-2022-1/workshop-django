from django import forms
from django.contrib.auth.models import User


class CadastraUsuario(forms.ModelForm):
    confirma_senha = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": "Nome de usuário",
            "password": "Senha",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder":"digite aqui um nome de usuário bonito"}),
            "password": forms.PasswordInput(attrs={"placeholder":"digite uma senha que preste"})
        }