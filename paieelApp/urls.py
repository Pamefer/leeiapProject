from django.conf.urls import include, url
from . import views
from views import send_command
urlpatterns = [
    url(r'^$', views.post_list),
    #url(r'^reconocimiento', views.reconocimiento),
    url(r'^reconocimiento', views.SubirFotoView.as_view(), name='reconocer'),
    url(r'^send_command$', send_command, name='send_command'),
    #url(r'^pruebaFormu$', send_command, name='send_command'),

]