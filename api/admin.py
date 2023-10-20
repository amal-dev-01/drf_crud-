from django.contrib import admin
from api.models import Students
# Register your models here.



class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city') 

admin.site.register(Students, StudentsAdmin)


