from django.conf.urls import url
from . import views

# Expressao regular:
# r -> raw text
#^ -> inicio do texto
#$ -> final do texto
# r'^$' -> expressao regular para texto vazio


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Testeeeee
    url(r'^teste/$', views.teste, name='teste'),
    # Exibir todos os topicos
    url(r'^topics/$', views.topics, name='topics'),
    # Pagina para um topico unico
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Get topic
    url(r'^topics/get/(?P<topic_id>\d+)/$', views.getTopic, name='getTopic'),
    # Pagina para adicionar um novo topico
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Página para adicionar nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Página para editar entrada
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
