from django.conf.urls import include, url
from . import views
from views import send_command
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^reconocimiento', views.reconocimiento),
    url(r'^send_command$', send_command, name='send_command'),

]