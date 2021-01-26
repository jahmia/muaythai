# -*- coding: utf-8 -*-
from datetime import timedelta

# from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class User(models.Model):

    def validate_six_years_or_older(value):
        min_date = value + timedelta(days=365 * 6)
        print(min_date, timezone.now())
        if min_date > timezone.now().date():
            raise ValidationError(message='6 years old is the minimum age requirement, please join us later.')

    inscription_date = models.DateField(default=timezone.now)
    birthday = models.DateField(validators=[validate_six_years_or_older])
    adress = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(unique=True)
    second_contact = models.CharField(verbose_name='Contact de secours',
        max_length=255,
        help_text="Personne à prévenir en cas d'accident", blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.email[:12]


class Arena(models.Model):

    """ Training Place
    """
    name = models.CharField(max_length=32)
    adress = models.CharField(max_length=255)
    notes = models.CharField(verbose_name='Description', max_length=255, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', 'active']


class Message(models.Model):
    name = models.CharField(max_length=32, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=16, blank=True)
    subject = models.CharField(max_length=64)
    message = models.TextField(max_length=1000)
