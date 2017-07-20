from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^teste$', views.teste, name='teste'),
]
