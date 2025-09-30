
from django.urls import path

from recipes.views import home


#dominio.com/recipes/
urlpatterns = [
    
    path("", home), #home
   
]
