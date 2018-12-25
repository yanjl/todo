from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import DoModel

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "indexes/index.html"


class DoListView(ListView):
    model = DoModel
    template_name = "indexes/do_list.html"
    # context_object_name = 'do_list'
