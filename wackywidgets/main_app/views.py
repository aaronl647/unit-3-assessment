from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Widget
from .forms import WidgetForm

class WidgetList(ListView):
  model = Widget

class WidgetDetail(DetailView):
  model = Widget

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'

class WidgetUpdate(UpdateView):
  model = Widget
  fields = '__all__'

class WidgetDelete(DeleteView):
  model = Widget
  success_url = ''

def home(request):
    widget = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'main.html', {
        'widget': widget, 'widget_form': widget_form
        })

