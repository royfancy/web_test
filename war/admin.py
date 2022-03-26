from django.contrib import admin

# Register your models here.
from .models import War # 取同資料內的 models.py 中的 War

admin.site.register(War) #這樣做才能註冊到後台