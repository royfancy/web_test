from django.contrib import admin

# Register your models here.
from .models import Russia # 取同資料內的 models.py 中的 War

admin.site.register(Russia) #這樣做才能註冊到後台