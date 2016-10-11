from django.shortcuts import redirect, render
from django.http import HttpResponse


def index(request):

    return HttpResponse('<div style="heigth:100%; background-color:lime;" >Yeees it works!!!</div>')
