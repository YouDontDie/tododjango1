from django.shortcuts import render, redirect
from .models import TodoList, Category, Human
import datetime


def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    humans = Human.objects.all()
    if request.method == "POST": #checking if the request method is a POS
        if "taskAdd" in request.POST: #checking if there is a request to add a tod
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            human = request.POST["human_select"] #category

            content = title + " -- " + date + " " + category + " " + human #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category), human=Human.objects.get(name=human))
            Todo.save() #saving the tod
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST: #checking if there is a request to delete a tod
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting tod
                todo.delete() #deleting tod
    return render(request, "index.html", {"todos": todos, "categories": categories, "humans": humans})

