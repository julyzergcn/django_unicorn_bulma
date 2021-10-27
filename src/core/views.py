from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render

from . import models


def homepage(request):
    return render(request, 'homepage.html')


def load_more(request):
    return render(request, 'load_more.html')


@require_POST
def delete_user(request, user_id):
    models.User.objects.filter(id=user_id).delete()
    return HttpResponse('')
