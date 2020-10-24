from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse(Path(__file__).resolve().parent.parent)
    return render(request, 'principal/index.html')
