from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def user_register(request):
    return HTTPResponse('USER REGISTER')