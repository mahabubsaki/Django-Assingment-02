from django.urls import path
from main.views import add_task,show_tasks,completed_tasks,delete_task,update_task,complete_task

urlpatterns = [
    path('',add_task,name='add_task'),
    path('show-tasks/',show_tasks,name='show_tasks'),
    path('completed-tasks/',completed_tasks,name='completed_tasks'),
    path('delete-task/<int:id>',delete_task,name='delete_task'),
    path('update-task/<int:id>',update_task,name='update_task'),
    path('complete-task/<int:id>',complete_task,name='complete_task'),
]
