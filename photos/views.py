from django.shortcuts import render ,redirect

# Create your views here.
from .forms import UploadModelForm
from .models import Photo

def index(request):
 	photos = Photo.objects.all() #抓取所有照片資料

 	form = UploadModelForm() #生成物件,準備來做表單驗證

 	if request.method == 'POST': #送出
 		form = UploadModelForm(request.POST,request.FILES) #UploadModelForm(request.POST,request.FILES) 對應函示 
 		if form.is_valid(): #表單驗證這裡是True和	Fales,進來的照片是 POST 和 image 的話
 			form.save() #儲存,存Server和資料庫
 			return redirect('/photos')  #導回去('/photos')儲存的地方
 	#沒送出的話,變成所有表單
 	context = { 
        'photos': photos,
        'form': form
    }

 	return render (request,'photos.html',context)


