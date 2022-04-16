from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widgets

# Define the home view

class AddWidgets(CreateView):
    model = Widgets
    fields = '__all__'
    sussess_url = '/'

    def get_context_data(self, **kwargs):
        kwargs['Widgets_list'] = Widgets.objects.order_by('id')
        return super(AddWidgets, self).get_context_data(**kwargs)
    
    

def index(request):
  return render(request, 'index.html')

def widget_delete(request, widget_id):
    widget = Widgets.objects.get(pk=widget_id)
    widget.delete()
    return redirect('add_widgets')