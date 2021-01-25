# -*- coding: utf-8 -*-
from django.forms import ModelForm

from fo.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'subject', 'message']