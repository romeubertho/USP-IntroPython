from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Home page"""
    return render(request,'index.html')
# testeeeeee
def teste(request):
    """Testeeeeeee"""
    return render(request,'teste.html')
# topics
def topics(request):
    """Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'topics.html',context)