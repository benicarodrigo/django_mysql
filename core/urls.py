from django.urls import path
from .views import produto, contato, index

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto,name='produto'),
]