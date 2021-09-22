from . import models
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

class DocumentListView(ListView):
    model = models.Document
    context_object_name = 'documents'
    template_name ='docai/document_list.html'
    documents = []
    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query)
        if query:
            return models.Document.objects.filter( Q(title__icontains=query) | Q(doc_summary__icontains=query))
        else:
            return models.Document.objects.all()