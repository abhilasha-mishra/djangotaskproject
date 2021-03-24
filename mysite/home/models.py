from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=1000, default="0")
    hed1 = models.CharField(max_length=1000, default="0")
    p1 = models.CharField(max_length=5000, default="0")
    hed2 = models.CharField(max_length=1000, default="0")
    p2 = models.CharField(max_length=5000, default="0")
    hed3 = models.CharField(max_length=1000, default="0")
    p3 = models.CharField(max_length=5000, default="0")
    image = models.ImageField(upload_to='blog/blogimages')
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user')
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


STATUS=((True, 'Yes'), (False, 'No'))
class Task(models.Model):
    title = models.CharField(max_length=200, null=True)
    task= models.CharField(max_length=200, null=True)
    status = models.BooleanField(choices=STATUS, default=False)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_task_user')
    created_date = models.DateTimeField(auto_now_add=True)


STATUS=((True, 'Yes'), (False, 'No'))
class ApplyTask(models.Model):
    ans=models.CharField(max_length=200)
    status = models.BooleanField(choices=STATUS, default=False)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name='taskcreated')
    created_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    created_date = models.DateTimeField(auto_now_add=True)


