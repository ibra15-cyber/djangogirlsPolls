from django.urls import path #urls 
from . import views  #views the code that will be rendered


urlpatterns = [
    path('', views.post_list),
   
]
