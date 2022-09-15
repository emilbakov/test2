from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from django.views import generic
from core.models import HuntSpot

# Create your views here.
class SpotListView(generic.ListView):
    model = HuntSpot
    paginate_by = 10

        
class SpotDetailView(generic.DetailView):
    model = HuntSpot

    
