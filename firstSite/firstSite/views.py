from django.http import HttpResponse

def home(request):
    return HttpResponse("Home this is the site")

def about(request):
    return HttpResponse("About")