from django import forms #django的forms 表單 
from .models import Photo #使用到models的Photo


#建立表單---驗證的地方
class UploadModelForm(forms.ModelForm): #準備上傳

	class Meta:
		model= Photo
		fields = ('image',)
		widgets = {'image':forms.FileInput(attrs={'class':'form-control-file'})
		}
			
			
