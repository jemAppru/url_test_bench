from django.shortcuts import render
from django.http import *

# Create your views here.
def Index(request):
    template_name = "main/index.html"
    return render(request=request, template_name=template_name, context={})

