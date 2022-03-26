"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from news.views import news,index

from product.views import products

from customer.views import customer,cusUpdate,login #1. cusUpdate 做修改會員資料 2.login 做會員註冊或登入

from contact.views import contact


from photos.views import index as pindex #多媒體區-放置照片 import index函示名稱 as pindex別名
                                                        #函示名稱相同,可以取別名
from sendmail.views import sendMail

#多媒體---setting 路勁 近來
from django.conf import settings
from django.conf.urls.static import static 

from cart.views import cart,addtocart,cartorder,cartok,cartordercheck,shopping

from war.views import war

from ukrayina.views import ukrayina

from russia.views import russia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',news),
    path('product/',products),
    path('customer/',customer),
    path('',index),  # 給客人用的網站
    path('index.html',index),
    path('contact/',contact),
    path('login/',login), #2.login 做會員註冊或登入
    path('cusUpdate/',cusUpdate), #1. cusUpdate 做修改會員資料
    path('photos/',pindex), #多媒體
    path('cart/',cart),
    path('addtocart/<str:ctype>/',addtocart),  #購物車 ,自訂義<str字串方式帶入:ctype在cart.views裡面>
    path('addtocart/<str:ctype>/<int:productid>/',addtocart),  #購物車,自訂義<str字串方式帶入:ctype>/<int整數:productid>/
    path('cartorder/',cartorder), #我要結帳-cart.html
    path('cartok/',cartok),     
    path('cartordercheck/',cartordercheck),
    path('sendmail/',sendMail), #信箱寄送
    path('wars/',war),
    path('ukrayinas/',ukrayina),
    path('russias/',russia),
    path('shopping/',shopping),
] 

#多媒體---setting 路勁 近來
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


