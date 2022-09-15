from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings



from django.urls import path
from . import views

urlpatterns = [   
    re_path('', views.SpotListView.as_view(), name='spots'),
    re_path('spot/<int:pk>/', views.SpotDetailView.as_view(), name='spot-detail'),

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)