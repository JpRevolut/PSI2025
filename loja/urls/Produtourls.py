from django.urls import path
from loja.views.Produtoview import list_produto_view
urlpatterns = [
path("", list_produto_view, name='produto'),
path("<int:id>", list_produto_view, name='details_produto'),
path("<int:id>", list_produto_view, name='edit_produto'),
path("<int:id>", list_produto_view, name='clear_produto'),
]