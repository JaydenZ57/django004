from django.shortcuts import render

# Create your views here.
def home(request):
    info = "Jayden"
    return render(request, "index.html", {"info": info})