from django import forms
from .models import Items
from django.contrib.auth.forms import UserCreationForm


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields=['item_name','item_desc','item_price','item_image']