from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from cloneapp.models import Region, Profile, Category, Listing

# def index(request):
#     return HttpResponse("Hello, this is the index page")


class IndexView(ListView):
    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        return Category.objects.filter()
