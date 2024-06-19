from django.urls import path
from.views import * # importndo tudo que existe no arquivo views
urlpatterns = [
    path('', homepage, name='homepage'), # carregando automaticamente todos os links do site (link/função que vai rodar quando abrir o site/nome interno(será o link da homepage))
    path('loja/', loja, name='loja'),
    path('minhaconta/', minha_conta, name='minha_conta'),
    path('login/', login, name='login'),
    path('carrinho/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout')
,
]
