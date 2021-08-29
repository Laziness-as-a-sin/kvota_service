from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'nologgin/index.html')
    # return HttpResponse("Как ты сюда попал?!!")
