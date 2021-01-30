from django.urls import path
from .views import cadastro_produto, contato, home, produto

urlpatterns = [
    path('', home, name='home'),
    path('produto/', produto, name='produto'),
    path('contato/', contato, name='contato'),
    path('cadastro_produto/', cadastro_produto, name='cadastro_produto'),
]