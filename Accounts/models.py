from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.



class usersignup(User):
    username = None
    
    email_token = models.CharField(max_length=100, null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    forgetpass_token = models.CharField(max_length=100, null=True,blank=True)
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = 'Account'
        
