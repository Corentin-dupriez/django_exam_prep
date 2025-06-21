from django.urls import path, include

from albums import views

urlpatterns = [
    path('', include([
        path('add/', views.AlbumAddView.as_view(), name='add_album'),
        path('<int:pk>/', include([
            path('details/', views.AlbumDetailView.as_view(), name='album_details'),
            path('edit/', views.AlbumEditView.as_view(), name='album_edit'),
            path('delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
        ]))]))
]