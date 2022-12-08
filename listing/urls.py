from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings



from django.urls import path
from . import views

urlpatterns = [   
    path('spots/', views.SpotListView.as_view(), name='spots'),

    # re_path('', views.SpotListView.as_view(), name='spots'),    
    re_path(r'spot/(?P<pk>\d+)/$', views.SpotDetailView.as_view(), name='spot-detail'),
    path(r'spotche/<int:id>/', views.detail_view)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)