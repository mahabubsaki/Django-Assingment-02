from django.shortcuts import render,redirect
from main.forms import TaskForm
from django.contrib import messages
from main.models import TaskModel

# Create your views here.
def add_task(request):
     if request.method == 'POST':
          form = TaskForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,"Task Added successfully.")
               return redirect("show_tasks")
     else:
          form = TaskForm()
     return render(request, 'add-task.html', {'form': form})

def completed_tasks(request):
     tasks = TaskModel.objects.filter(is_completed=True)
     return render(request,'completed-tasks.html',{'tasks':tasks})

def show_tasks(request):
     tasks = TaskModel.objects.filter(is_completed=False)
     return render(request,'show-tasks.html',{'tasks':tasks})

def delete_task(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect("show_tasks")
def update_task(request,id):
     task = TaskModel.objects.get(pk = id)
     if request.method == 'POST':
          form = TaskForm(request.POST, instance=task)
          if form.is_valid():
               form.save()
               return redirect('show_tasks')
          else:
               return render(request,"update-task.html",{'form':form})
     form = TaskForm(instance=task)
     return render(request,"update-task.html",{'form':form})

def complete_task(request,id):
     task = TaskModel.objects.get(pk = id)
     task.is_completed = True
     task.save()
     messages.success(request,"Task Completed")
     return redirect('completed_tasks')