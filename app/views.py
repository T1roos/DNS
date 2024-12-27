from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import TopBlockItems


# Create your views here.
class ProductListView(ListView):
    model = TopBlockItems
    template_name = 'index.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = TopBlockItems
    fields = "__all__"
    template_name = ''
    success_url = reverse_lazy('')


class ProductUpdateView(UpdateView):
    model = TopBlockItems
    fields = "__all__"
    template_name = ''
    success_url = reverse_lazy('')


class ProductDeleteView(DeleteView):
    model = TopBlockItems
    template_name = ''
    success_url = reverse_lazy('')


class ProductDetailView(DetailView):
    model = TopBlockItems
    template_name = ''
