from django.http import HttpResponse

def home(request):
    return HttpResponse("Halo! Ini proyek portofolio django pertamaku")
