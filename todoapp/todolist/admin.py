from django.contrib import admin
from . models import ToDoItem, Tag


admin.site.register(ToDoItem)
admin.site.register(Tag)


