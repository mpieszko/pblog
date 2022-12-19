from django import forms

#-- Formulario para los contactos, de la tabla Contacto:
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
#--        
