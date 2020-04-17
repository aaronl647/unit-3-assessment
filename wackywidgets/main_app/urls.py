from django.urls import path

from . import views

urlpatterns = [
      path('', views.home, name='home'),
      # path('', views.add_widget, name='add_widget'),
      path('', views.WidgetCreate.as_view(), name='widget_create'),
      path('', views.WidgetDelete.as_view(), name='widget_delete'),



]