from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>Home view madafaka</p>')

def contest_detail(request, id):
    return HttpResponse('<p>In contest_detail view with name {0}</p>'.format(id))
