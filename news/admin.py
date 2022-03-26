from django.contrib import admin

# Register your models here.
from .models import News  # 取同資料內的 models.py 中的 News

admin.site.register(News) #這樣做才能註冊到後台

    
    
    
    
    
    
    
    