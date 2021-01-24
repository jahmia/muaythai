# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'fo/home.html', {'home': 'active'})


def club(request):
    return render(request, 'fo/club.html', {
        'club': 'active',
        'title': 'Yanakmuay 19 - Le club'
    })


def coachs(request):
    return render(request, 'fo/coach.html', {
        'coach': 'active',
        'title': "Yanakmuay 19 - Les coachs"
    })


def course(request):
    return render(request, 'fo/course.html', {
        'course': 'active',
        'title': "Yanakmuay 19 - Les cours"
    })


def register(request):
    return render(request, 'fo/register.html', {
        'register': 'active',
        'title': "Yanakmuay 19 - Inscription"
    })


def contact(request):
    return render(request, 'fo/contact.html', {
        'contact': 'active',
        'title': "Yanakmuay 19 - Nous contacter"
    })
