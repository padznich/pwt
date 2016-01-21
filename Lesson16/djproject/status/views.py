
import sys
import django
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def showPyDjStatus(request):
    py_version = sys.version[:3]
    dj_version = django.__version__
    return HttpResponse("<h1>Python version is: {}<h1>"
                        "<h1>Django version is: {}<h1>".format(py_version, dj_version))