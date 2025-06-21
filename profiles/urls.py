from django.urls import path

from profiles.views import ProfileDetailView, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetailView.as_view(), name='profile_details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]