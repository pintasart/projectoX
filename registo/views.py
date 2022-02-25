from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistoForm

# Create your views here.


def registo(request):

    if request.method == "POST":

        form = RegistoForm(request.POST)
        
        print("--------1--------")
        print(request.POST)
        print("--------2--------")
        print(form.is_valid()) #True
        print("--------2a--------")
        print(form.formFilhos.is_valid()) #False
        print("-----------------")

        if form.is_valid() and form.formFilhos.is_valid():
            # nome = form.cleaned_data['nome'],
            # sexo = form.cleaned_data['sexo'],
            print(form.cleaned_data)
            return HttpResponseRedirect('<h1>Registo OK.</h1>')
        else:
            print("NOT VALID")
            dicio = {
                "form": form,
            }
            return render(request, 'registo/registo.html', context=dicio)

    elif request.method == "GET":
        return render(request, 'registo/registo.html', context={'form': RegistoForm()})
