from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    # return HttpResponse("<h1>Начальная страница</h1>")
    return render(request, "mainapp/index.html", {})
