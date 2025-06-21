from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from albums.models import Album
from profiles.forms import ProfileCreateForm
from common.utils import get_profile

# Create your views here.
class HomePageView(ListView, BaseFormView):
    form_class = ProfileCreateForm
    model = Album
    context_object_name = 'albums'

    def get_queryset(self):
        queryset = Album.objects.all()
        return queryset

    def get_template_names(self):
        if not get_profile():
            return 'home-no-profile.html'
        return 'home-with-profile.html'
    
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)
            
    def get_success_url(self):
        return reverse_lazy('home')
