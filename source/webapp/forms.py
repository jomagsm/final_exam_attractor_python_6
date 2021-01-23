from django import forms

from webapp.models import Message


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['description']