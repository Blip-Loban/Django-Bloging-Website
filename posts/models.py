from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category= models.ManyToManyField(Category) #One post can have multipple category and vice versa
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title 