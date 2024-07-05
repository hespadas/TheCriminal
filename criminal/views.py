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

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


def home(request):
    context = {'name': 'John Doe'}
    return render(request, 'criminal/home.html', context)

