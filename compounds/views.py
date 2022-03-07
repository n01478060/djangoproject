from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
import requests
from .forms import MWForm
from django.shortcuts import redirect
from .mw_calculator import MWcalculator


def compounds_list(request):
    compounds = Compound.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compounds/compounds_list.html', {'compounds': compounds})


def compound_detail(request, pk):
    compound = get_object_or_404(Compound, pk=pk)
    compound_InChIKey = compound.InChIKey
    pubchem_request = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+compound_InChIKey+"/synonyms/json").json()
    pubchem_request_synonym = pubchem_request['InformationList']['Information'][0]['Synonym']
    return render(request, 'compounds/compound_detail.html', {'compound': compound, 'request': pubchem_request_synonym})


def computed_mw(request):
    computed = Computed_Molecular_Weight.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compounds/computed_mw.html', {'computed': computed})


def computed_mw_new(request):
    if request.method == "POST":
        form = MWForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.calculated_molecular_weight = str(MWcalculator(post.molecular_formula))
            pub_request_mw = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+post.inchikey+"/property/MolecularWeight/json")
            post.pubchem_molecular_weight = str(pub_request_mw.json()["PropertyTable"]["Properties"][0]["MolecularWeight"])
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('computed_mw')
    else:
        form = MWForm()
    return render(request, 'compounds/computed_mw_new.html', {'form': form})


def compound_data(request, pk):
    compound_data_hold = get_object_or_404(Compound_Data, pk=pk)
    return render(request, 'compounds/compound_data.html', {'compound_data': compound_data_hold})
