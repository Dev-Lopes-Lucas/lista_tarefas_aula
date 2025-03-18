from django.shortcuts import render

# Create your views here.

def home ( request):
    tasks = Task.objects.all() #dados do banco
    return render(request, 'index.html', {'tasks': [1,2,3]} )