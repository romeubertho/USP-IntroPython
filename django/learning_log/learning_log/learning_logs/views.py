from django.shortcuts import render

# Create your views here.
def index(request):
    """Home page"""
    return render(request,'index.html')
# testeeeeee
def teste(request):
    """Testeeeeeee"""
    return render(request,'teste.html')