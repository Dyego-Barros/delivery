from django import forms
from django.forms import HiddenInput
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city','payment', 'troco']
        widgets ={'key_order': forms.HiddenInput()}
        labels= {'first_name': 'Nome',
                 'last_name': 'Sobrenome',
                 'email': 'E-mail',
                 'address': 'Endereço',
                 'postal_code': 'Bairro',
                 'city': 'Cidade',
                 'payment': 'Forma de Pagamento',
                 'troco': 'Troco'}
        
