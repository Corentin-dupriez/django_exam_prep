from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

from albums.forms import AlbumCreateForm, AlbumUpdateForm, AlbumDeleteForm
from albums.models import Album


# Create your views here.
class AlbumAddView(CreateView):
    model = Album
    queryset = Album.objects.all()
    form_class = AlbumCreateForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album-details.html'

class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumUpdateForm
    template_name = 'album-edit.html'
    success_url = reverse_lazy('home')

class AlbumDeleteView(DeleteView, FormView):
    model = Album
    template_name = 'album-delete.html'
    success_url = reverse_lazy('home')
    form_class = AlbumDeleteForm

    def get_initial(self):
        pk = self.kwargs.get('pk')
        obj = self.model.objects.get(pk=pk)
        initial = obj.__dict__
        return initial
    
