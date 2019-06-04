from django.contrib import admin

# Register your models here.
from .models import Emp

class AdminEmp(admin.ModelAdmin):
    list_display = ['eid','ename','esal','created','modified']

admin.site.register(Emp,AdminEmp)