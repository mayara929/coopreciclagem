from django.shortcuts import render
#from django.http import HttpResponse
def home(request):
    #return HttpResponse("<h1>Ola mundo Ufra/<?h1>")
    return render(request,"index.html")

# Create your views here