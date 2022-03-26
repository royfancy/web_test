from django.contrib import admin

# Register your models here.


from .models import Photo 

#後台會顯示圖片和時間('image', 'upload_date')
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'upload_date')


admin.site.register(Photo, PhotoAdmin)