
from django.urls import path


from recipes import views


# dominio.com/recipes/
urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipe),  # detalhe da receita
]
