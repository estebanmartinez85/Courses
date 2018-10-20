from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request) -> JsonResponse:
    return JsonResponse({"home": "home!!"})


def about(request) -> JsonResponse:
    return JsonResponse({"about": "about!!"})


def login(request) -> JsonResponse:
    return JsonResponse({"r": "LOGIN"})


