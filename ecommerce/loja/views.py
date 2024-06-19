from django.shortcuts import render

# Create your views here.
# funções para os links criados
def homepage(request):
    return render(request, 'homepage.html') # rederizador
def loja(request):
    return render(request, 'loja.html') # rederizador
def carrinho(request):
    return render(request, 'carrinho.html') # rederizador
def checkout(request):
    return render(request, 'checkout.html') # rederizador
def minha_conta(request):
    return render(request, 'usuario/minhaconta.html') # rederizador
def login(request):
    return render(request, 'usuario/login.html') # rederizador