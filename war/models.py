from django.db import models

# Create your models here.
class War(models.Model):
    title = models.CharField(max_length=50)   #欄位名稱 = 文字單行輸入字串(最大長度)
    
    content = models.TextField()       #內容 =  文字多行輸入()
    
    photo_file = models.CharField(max_length=200)
    
    video_url = models.CharField(max_length=200)
    
    create_date = models.DateField(auto_now_add = True) #只有在物件建立時,才會新增日期auto_now_add = True
    
    
    class Meta:
        
        db_table = 'war' #建立資料表table = wars