
from django.urls import path


from recipes import views


# dominio.com/ (este arquivo é incluído em projeto/urls.py sem prefixo)
app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.recipe, name='recipe'),  # detalhe da receita
    path('search/', views.search, name='search'),
]
