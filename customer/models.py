from django.db import models





# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30,null = False) #null空值 = False 不允許
    
    sex = models.CharField(max_length=2,default='F',null = False) #預設 default='F' 
    
    birthday = models.DateField()
    
    email = models.EmailField(max_length=70,blank=True,default='') #blank 必填=True 一定要
    
    phone = models.CharField(max_length=10,blank=True,default='')
    
    address = models.CharField(max_length=200,blank=True,default='')
    
    password = models.CharField(max_length=100,null = False)
    
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table='customer'
    
    
    
    
    
    
    
    
    
    
    