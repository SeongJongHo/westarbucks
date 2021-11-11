
from django.http import  HttpResponse
def ping(request):
    return HttpResponse("pong")
# Create your views here.
