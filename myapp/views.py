from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    res=HttpResponse("""<html><body bgcolor=green><
                    h1><center>myapp space karthik</center></h1></body></html>""")
    return res
def welcome(request):
    res=HttpResponse("""<html><body bgcolor=green><
                    h1><center>myapp space karthik</center></h1></body></html>""")
    return res
