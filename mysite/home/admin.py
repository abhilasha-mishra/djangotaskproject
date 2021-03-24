from django.contrib import admin
from .models import BlogPost,Task,ApplyTask
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Task)
admin.site.register(ApplyTask)