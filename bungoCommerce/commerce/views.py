# pyright: reportGeneralTypeIssues=false

from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    return render(request, "commerce/index.html",
                  {"products": Product.objects.all()})
