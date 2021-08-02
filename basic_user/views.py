from django.http.request import HttpRequest
from django.shortcuts import render
from basic_user.services import Kek
from django.http import HttpResponse

# Create your views here.
def kek_request(request):
    return HttpResponse("Как ты сюда попал?!")
