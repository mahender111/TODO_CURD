from django.contrib import admin
from myapp.models import student, ToDoList,ToDoItem

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display= ('id','name','age','email')

admin.site.register(student,StudentAdmin)


class ToDoListAdmin(admin.ModelAdmin):
    list_display= ('id','title',)

admin.site.register(ToDoList,ToDoListAdmin)

class ToDoItemAdmin(admin.ModelAdmin):
    list_display= ('id','title','description','created_date', 'due_date', 'todo_list')

admin.site.register(ToDoItem,ToDoItemAdmin)
