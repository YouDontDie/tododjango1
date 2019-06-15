# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# create your models here.
class Human(models.Model):
	name = models.CharField(max_length=50, verbose_name="Имя")
	surname = models.CharField(max_length=50, verbose_name="Фамилия")
	birth = models.DateField(auto_now_add=False, auto_now=False)
	salary = models.IntegerField()

	class Meta:
		verbose_name = ("human")
		verbose_name_plural = ("humans")

	def __str__(self):
		return self.name #name to be shown when called

class Category(models.Model): # the category table name that inherits models.model
	name = models.CharField(max_length=100) #like a varchar

	class Meta:
		verbose_name = ("category")
		verbose_name_plural = ("categories")

	def __str__(self):
		return self.name #name to be shown when called



class TodoList(models.Model): #Todolist able name that inherits models.Model
	title = models.CharField(max_length=250) # a varchar
	content = models.TextField(blank=True) # a text field
	human = models.ForeignKey(Human, default="general", on_delete=models.CASCADE,)
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE,) # a foreignkey


	class Meta:
		ordering = ["-created"] #ordering by the created field

	def __str__(self):
		return self.title #name to be shown when calledd

