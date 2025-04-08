from django.urls import path
from .views import *


urlpatterns = [
    path('tasks', listar, name='home'),
    path('tasks/<int:task>/', update, name = 'edicao'),
    path('tasks/<int:task>/delete', delete, name='delete')

]