from django.shortcuts import render

from django.http import HttpResponseRedirect #HttpResponseRediect 重新指向到那一個網址去


from .models import Customer

import hashlib # 加密

# Create your views here.
def customer(request):
    
    if 'username' in request.POST:
        
        username = request.POST['username']
        
        sex = request.POST['sex']
        
        birthday = request.POST['birthday']
        
        email = request.POST['Email']
        
        phone = request.POST['phone']
        
        address = request.POST['address']
        
        password = request.POST['pwd']
        
        Customer.objects.create(name = username, sex = sex, birthday = birthday, 
                                email = email, phone = phone, address = address, 
                                password = password)
        
     
    if request.session.get('Ulogined',False):   #若使用者已經登入時,就跳轉到customer.html

        return render(request,'customer.html')

    else:                            
        return HttpResponseRedirect('/login/')  #若使用者未登入時,就跳轉到login

    #return render(request,'customer.html')



def cusUpdate(request): #1. cusUpdate 修改會員資料


    if 'password' in request.POST: #由密碼 得知帳號
    
        mail = request.session['userEmail']
        pwd = request.POST['password']  #密碼是明碼

        obj = Customer.objects.get(email = mail)

        pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest() #密碼加密

        obj.password = pwd

        
        obj.save()
        
    return render(request,'updateCus.html')
        
        
def login(request):  # 2.login 做會員註冊或登入
    if 'username' in request.POST:
        user = request.POST['username']  #使用者的 email 當帳號
        pwd = request.POST['password']   #使用者的密碼
        
        pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest() #密碼加密

        #使用get
        #obj = Customer.objects.get(email=user,password=pwd) 
        #或 obj = Customer.objects.filter(email=user,password=pwd).count() 

        #如果使用get時,資料庫中一定要有資料才可以
        #不然資料庫會發生錯誤  DoesNotExist at /login/


#---------------------資料庫確認有無資料----------------------------------------
        #使用 filter...count()
        obj = Customer.objects.filter(email=user,password=pwd).count()
        if obj > 0 :
            request.session['Ulogined'] = True #session = True將使用者資料記憶在主機端,瀏覽器關閉時就消失
            request.session['userEmail'] = user #修改 userEmail 為id
            return HttpResponseRedirect('/')

        else:

            return render(request,'login.html')

#-------------------------------------------------------------------------
    else:
        if request.session.get('Ulogined',False):
            del request.session['Ulogined']
            if request.session.get('userEmail','') != '': #預設不是空直 就殺掉
                del request.session['userEmail']
        return render(request,'login.html')







