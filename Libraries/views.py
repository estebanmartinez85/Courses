from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Libraries.models import Library
from django.core import serializers
# Create your views here.


def index(request) -> JsonResponse:
    libraries = Library.objects.values()
    #libraries_json = serializers.serialize('json', libraries)
    return JsonResponse(list(libraries), safe=False)

