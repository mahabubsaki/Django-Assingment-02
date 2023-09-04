from django import forms
from main.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed']
        widgets= {
            'taskTitle':forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'taskTitle','placeholder':' '}),
            'taskDescription':forms.TextInput(attrs={'class':'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer','id':'taskDescription','placeholder':' '}),
      
            'is_completed':forms.CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500  focus:ring-2','id':'is_completed'})
        }