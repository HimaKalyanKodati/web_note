from django.urls import path
#importing views
from . import views

app_name = 'noteapp'
urlpatterns = [
    # path('',views.showNote,name='show'),
    path('',views.showNote.as_view(),name='show'),
    # path('edit/<int:note_id>',views.editNote,name='edit'),
    path('edit/<int:pk>/',views.editNote.as_view(),name='edit'),
    # path('create/',views.createNote,name='create'),
    path('create/',views.createNote.as_view(),name='create'),
    # path('delete/<int:note_id>',views.deleteNote,name='delete'),
    path('delete/<int:pk>/',views.deleteNote.as_view(),name='delete'),
]
