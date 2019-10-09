from django.conf.urls import url
from lists import views

urlpatterns = [url("^$", views.home_page, name="home")]
