from django.contrib import admin

# Register your models here.


from .models import Products  # 取同資料內的 models.py 中的 Products

admin.site.register(Products) #這樣做才能註冊到後台