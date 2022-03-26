from django.shortcuts import render

# Create your views here.
from datetime import datetime
from .models import Ukrayina

import requests
import json


def index(request):

  return render(request,'index.html')

def ukrayina(request):
    
   #  #爬蟲-json解析
   #  url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json' #1.網址
   #  data = requests.get(url).text   #2.載下來變成文字檔
   #  bike = json.loads(data)        #3.json檔格式
   #  station = list()
   #  for item in bike:
   #      station.append(item['StationName'])
     
     
    
   #  score = [100,89,60,70]
   #  content ={'score':score,'display_time':str(datetime.now()),'ubike':station}
   #  #return render(request,  'news.html',{'display_time':str(datetime.now())})
    
   #  return render(request,  'news.html',content)
   # #可以寫成這樣return render(request,  'news.html',locals())結果與上面相同
   # #return render(request,  'news.html',locals())
   # #                                    locals()--打包
       
    
    
       
        allukrayina = Ukrayina.objects.all().order_by('id') #.order_by排序('id':遞增,'-id':遞減)
        content = {'ukrayina':allukrayina} #資料庫名稱相符
        return render(request,'ukrayina.html',content)
