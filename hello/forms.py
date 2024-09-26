from django import forms
from hello.models import Order, UsersDog

class OrderForm(forms.ModelForm):
    dog = forms.ModelChoiceField(queryset=UsersDog.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('dog', 'name', 'phone')
