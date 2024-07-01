from django.contrib import admin
from django.urls import path

from criminal.views import home, CriminalListView, CriminalCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('list/',  CriminalListView.as_view(), name='criminal_list'),
    path('create/',  CriminalCreateView.as_view(), name='criminal_create'),
]
