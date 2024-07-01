from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models.criminal import Criminal

class CriminalListView(ListView):
    model = Criminal


class CriminalCreateView(CreateView):
    model = Criminal
    fields = ['name', 'criminal_classification_id',]
    success_url = reverse_lazy('criminal_list')


def home(request):
    context = {'name': 'John Doe'}
    return render(request, 'criminal/home.html', context)


# def get_criminal_list(request):
#     criminals = Criminal.objects.all()
#     return HttpResponse('This is the criminal list')
#
#
# def create_criminal(request):
#     return render(request, 'criminal/create_criminal.html')
#
#
