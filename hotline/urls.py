from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # New ticket
    path('new/', views.new_ticket, name='new_ticket'),
]