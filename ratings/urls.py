from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.item_list, name='item_list'),
]
