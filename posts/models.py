from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category= models.ManyToManyField(Category) #One post can have multipple category and vice versa
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self):
        return self.title 

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commented by {self.name}'