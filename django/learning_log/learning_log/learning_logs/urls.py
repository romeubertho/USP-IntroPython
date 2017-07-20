from django.conf.urls import url
from . import views

#Expressao regular:
    #r -> raw text
    #^ -> inicio do texto
    #$ -> final do texto
    #r'^$' -> expressao regular para texto vazio
    

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Testeeeee
    url(r'^teste$', views.teste, name='teste'),
]
