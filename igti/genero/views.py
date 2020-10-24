from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponseNotAllowed
# Create your views here.


def cadastro(request):
    form_criado = forms.GeneroForm()
    if request.method == 'POST':
        print("Salvando os dados...")
        form = forms.GeneroForm(request.POST)
        print(form)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR")
    generos_list = models.Genero.objects.order_by('descricao')
    data_dict = {'form': form_criado, 'generos_records': generos_list}
    return render(request, 'genero/genero.html', data_dict)


def delete(request, id):
    try:
        models.Genero.objects.filter(id=id).delete()
        form_criado = forms.GeneroForm();
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form_criado, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed


def update(request, id):
    item = models.Genero.objects.get(id=id);
    if request.method == 'GET':
        form_criado = forms.GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form': form_criado}
        return render(request, 'genero/genero_upd.html', data_dict)
    elif request.method == 'POST':
        form_criado = forms.GeneroForm(request.POST)
        item.descricao = form_criado.data['descricao']
        item.save()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form_criado, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)
