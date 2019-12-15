from django.shortcuts import render, redirect
from .forms import AdoptanteForm, MascotaForm, FichaForm

# Create your views here.
def Home(request): 
    return render(request, 'index.html')

def ingresoAdoptante(request):
    if request.method == 'POST':
        adoptante_form = AdoptanteForm(request.POST)
        if adoptante_form.is_valid():
            adoptante_form.save()
            return redirect('index')
        else:
            adoptante_form =  AdoptanteForm()   
        return render(request, 'rescatados/ingresoAdoptante.html', {'adoptante_form':adoptante_form})

        