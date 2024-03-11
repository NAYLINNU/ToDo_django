from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name='addTask'),
    path('mark/<int:pk>/',views.mark, name='mark'),
    path('unmark/<int:pk>/',views.unmark, name='unmark'),
    path('taskedit/<int:pk>/',views.taskedit, name='taskedit'),
    path('taskdelete/<int:pk>/',views.taskdelete, name='taskdelete'),



]