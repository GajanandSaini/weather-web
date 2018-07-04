from django.conf.urls import url
from weather_app import views

urlpatterns = [
    url(r'^$',views.index),
]
