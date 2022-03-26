from django.shortcuts import render

# Create your views here.
from .models import Products


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#                           Paginator分頁,EmptyPage空白頁,PageNotAnInteger 非整數
def products(request):
    
    pname = ''
    
    if 'qp' in request.GET:
        pname = request.GET['qp']
        pData =  Products.objects.filter(name__contains=pname)
        
    else :
         
    #變化版
        pData = Products.objects.all().order_by('-id')
    #pData = Products.objects.all().order_by('-id')[:10]  #抓取 排序後前10筆資料
    #pData = Products.objects.filter(price='2084')  #過濾 -找價格是2084的產品
    #pData = Products.objects.exclude(price='2084') #不等於 -找出不等於2084的產品
    
    #pData = Products.objects.get(id=2) #唯一性 
    
    #pData = Products.objects.filter(price__gt=1500)  #過濾 -找價格大於1500的產品
    #pData = Products.objects.filter(price__gte=1500) #過濾 -找價格大於等於1500的產品
    
    #pData = Products.objects.filter(price__lt=1500)  #過濾 -找價格小於1500的產品
    #pData = Products.objects.filter(price__lte=1500) #過濾 -找價格小於等於1500的產品
    
    #pData = Products.objects.filter(price__gte=1000,price__lte=2000)  #過濾 -找價格介於1000~2000的產品
    #pData = Products.objects.filter(price__range=[1000,2000])          #過濾 -找價格介於1000~2000的產品
    
    #pData = Products.objects.filter(name__contains='休閒鞋')   #過濾-只要有的產品(包含)都出來---% 休閒鞋 %
    #pData = Products.objects.filter(name__startswith='NIKE KD')     #過濾-只要名字前面有的的產品都出來--- 休閒鞋 %
    #pData = Products.objects.filter(name__endswith='4100')     #過濾-只要名字後面有的的產品都出來---% 休閒鞋  
       
    
    paginator = Paginator(pData, 8)  #做分頁--8筆資料會一分頁
    
   # page = request.GET['page']     #抓取第幾頁
    page = request.GET.get('page')  #有參數就直接拿
    
    
    try :
        pData = paginator.page(page)
    
    except PageNotAnInteger: #若是空白頁
        pData = paginator.page(1) #回到第一頁
    
    except EmptyPage:
        pData = paginator.page(paginator.num_pages)  #回到總分頁
       
    content = {'product': pData,pname:'pname'}
    return render(request,'product.html',content)