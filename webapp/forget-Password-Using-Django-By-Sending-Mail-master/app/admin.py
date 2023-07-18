from django.contrib import admin
from .models import Profile
# Register your models here.
admin.site.register(Profile)

from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']