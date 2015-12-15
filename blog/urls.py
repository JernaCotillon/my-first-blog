<<<<<<< HEAD
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
=======
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    ]
>>>>>>> 1b30612c0046178ecf21f89ab435590cddefd6df
