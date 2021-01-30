from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def home(requests):
    return render(requests, 'home.html')


def produto(requests):
    context = {
        'produtos': Produto.objects.all()

    }
    return render(requests, 'produto.html', context)


def contato(requests):
    form = ContatoForm(requests.POST or None)
    if str(requests.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(requests, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(requests, 'Erro ao enviar e-mail!')

    context = {
        'form': form
    }
    return render(requests, 'contato.html', context )


def cadastro_produto(requests):
    if str(requests.user) != 'AnonymousUser':
        if str(requests.method) == 'POST':
            form = ProdutoModelForm(requests.POST, requests.FILES)
            if form.is_valid():
                form.save()
                messages.success(requests, 'Produto Salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(requests, 'Erro ao salvar o produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(requests, 'cadastro_produto.html', context)
    else:
        return redirect('home')




