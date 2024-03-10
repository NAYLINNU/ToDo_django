from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):  #take care list_display and search_fields din't wrong
    list_display = ('task','is_completed','created_at','updated_at')
    search_fields = ('task',)



admin.site.register(Task,TaskAdmin)