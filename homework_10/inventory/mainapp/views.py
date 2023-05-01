from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Device, Card


def index_view(request):
    # return HttpResponse("<h1>Начальная страница</h1>")
    cards = Card.objects.all()
    return render(request, "mainapp/index.html", {'cards': cards})


class DeviceListView(ListView):
    model = Device


class DeviceDetailView(DetailView):
    model = Device


class DeviceCreateVIew(CreateView):
    model = Device
    fields = '__all__'
    success_url = '/device-list/'