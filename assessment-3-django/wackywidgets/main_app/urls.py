from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddWidgets.as_view(), name='add_widgets'),
    path('', views.DeleteView.as_view(), name='delete_widgets')
]