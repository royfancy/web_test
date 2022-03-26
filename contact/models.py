from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,null = False) #null空值 = False 不允許
               
    email = models.EmailField(max_length=100,blank=True,default='') #blank 必填=True 一定要
    
    subject = models.CharField(max_length=100,blank=True,default='')
            
    content = models.TextField()
    
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table='contact'