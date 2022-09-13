from django.contrib import admin
from .models import Students


# admin.site.register(Students)
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','age']
    # list_editable = ['age']
    # list_filter = ['age']
