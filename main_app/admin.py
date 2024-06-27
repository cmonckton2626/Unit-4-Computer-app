from django.contrib import admin
from .models import Computer, Comment, Peripheral

# Register your models here.
admin.site.register(Computer)
admin.site.register(Comment)
admin.site.register(Peripheral)
