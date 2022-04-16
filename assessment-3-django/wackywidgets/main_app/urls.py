from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddWidgets.as_view(), name='add_widgets'),
    path('<int:widget_id>/delete/', views.widget_delete, name='delete_widgets')
]