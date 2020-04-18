from django.shortcuts import render, redirect
from .models import *
from .forms import WidgetForm

# Create your views here.
def home(request):
    widgets_list = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'main.html', {
		'widget_list': widgets_list, 
		'widget_form': widget_form
		})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')

def delete_widget(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('home')

