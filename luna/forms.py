from django.db.models import fields
from luna.models import Usuario
from django import forms
from django.forms.models import ModelFormMetaclass
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre']