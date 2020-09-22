from django.shortcuts import render
from .models import Todo
import datetime
from django.http import HttpResponseRedirect , JsonResponse

def homepage(request):
	todoItems = Todo.objects.all()#.order_by("-added_date")
	if request.is_ajax():
		return JsonResponse(todoItems,safe="False")
	return render(request,"index.html", { "todoItems":todoItems })

def addtodo(request):
	date = datetime.datetime.now()
	data = request.POST['content']
	crt_obj = Todo.objects.create(added_date=date , text=data)
	return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
	Todo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect("/")