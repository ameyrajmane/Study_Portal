from django.contrib import admin

from dashboard.models import *
from django.contrib import admin
# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)