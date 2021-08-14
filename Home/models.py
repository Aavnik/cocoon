from django.db import models
import uuid
from Accounts.models import *


# Create your models here.
class Basemodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Category(Basemodel):

    cust = models.ForeignKey(usersignup, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(Basemodel):
    custphoto = models.ForeignKey(usersignup, on_delete=models.CASCADE,null=True,blank=True)
    Category =models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to ='Image')

    class Meta:
        ordering = ['-created_at']
   