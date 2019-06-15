
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

class TodoListAdmin(admin.ModelAdmin):
	list_display = ("title", "created", "due_date")

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)

class HumanAdmin(admin.ModelAdmin):
	list_display = ("name",)

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Human, HumanAdmin)