
# Create your views here.
from django.shortcuts import render, get_object_or_404
from core.models import HuntSpot
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class SpotListView(ListView):
    model = HuntSpot
    paginate_by = 10

        
class SpotDetailView(DetailView):
    model = HuntSpot
    templates_name: 'huntspot_detail.html'
    def get_context_data(self, **kwargs):
        context = super(SpotDetailView, self).get_context_data(**kwargs)        
        print(context)
        return context 


def detail_view(request, id):
    spot=get_object_or_404(HuntSpot, id=id)
    # photos = SpotImages.objects.filter(spot=spot)
    context = {
        'spot':spot,
        # 'photos':photos
    }
    return render(request,'detail.html', context)