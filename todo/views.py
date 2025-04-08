from django.shortcuts import render
from .models import Task
from .forms import TaskForm
import json
from django.http import JsonResponse

# Create your views here.

def listar(request):
    print('qualqurfejf' ,request)
    if request.method == 'GET':
        tasks = Task.objects.all() #dados do banco
        form = TaskForm()
        return render(request, 'index.html', {'tasks': tasks, 'form':form} )
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        

        form = TaskForm(data)
        if form.is_valid():
            task = form.save()
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed}, status=201)
    return JsonResponse({'error': 'Invalid data'}, status=400)

def update(request,task):

    data= json.loads(request.body)

    new_completed = data.get('completed', False)
    try:
        task = Task.objects.get(id=task)
    except:
        return JsonResponse({"message":"Não encontrado"}, status=404)
    
    task.completed = new_completed
    task.save()

    return JsonResponse({"message":"OK"}, status=200)



def delete(request, task):
    try:
        task = Task.objects.get(id=task)
        if request.method == "DELETE":
            task.delete()
            return JsonResponse({'message': 'Task deleted'}, status=204)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
    


