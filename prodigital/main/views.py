# Create your views here.
from django.http import HttpResponse

def home(request):
	html="<html><head><title>Ya es hora</title></head><body><h1>Vamos!!!!</h1></body></html>"
	return HttpResponse (html)
