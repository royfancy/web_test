from django.shortcuts import render,redirect
from cart import models
from product.models import Products #使用 Products 資料夾
import os

basedir = os.path.dirname(__file__)

file = os.path.join(basedir,'ecpay_payment_sdk.py')

import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
from datetime import datetime


# Create your views here.

#from sendmail.views import sendmail # 呼叫 sendmail

cartlist = list() #購物車列表
customname = ''
customphone = ''
customaddress = ''
customemail = ''

def cart(request): #顯示購物車內容
	global cartlist 
	allcart = cartlist
	total = 0
	for unit in cartlist: #計算商品總額
		total += int(unit[3]) #3是 抓取 models.py 排列中grandtotal及unitprice

	grandtotal = total+60 #加運費
	return render(request,'cart.html',locals())

#-----------------------------------------------------------------------
#加入購物車
def addtocart(request,ctype=None,productid=None):
    global cartlist #購物車列表
    if ctype == 'add' : #定義加入購物車,沒有存到資料庫
        product = Products.objects.get(id=productid) #商品
        flag = True #
        for unit in cartlist: #若商品存在的話
            if product.name == unit[0]:   #
                unit[2] = str(int(unit[2])+1) #數量加1
                unit[3] = str(int(unit[3])+product.price) #累計金額			
                flag = False ; #表示商品之前已存在於購物車中
                break

        if flag: #代表商品沒有存在於購物車中
            templist = list() #暫存
            templist.append(product.name) #商品名稱
            templist.append(str(product.price)) #商品價格
            templist.append('1') #預設數量 1
            templist.append(str(product.price)) #總價
            cartlist.append(templist) #加入購物車

        request.session['cartlist'] = cartlist #將購物車內容存入session
        return redirect('/cart/')


#---------------------------------------------------------------------       
	#更新購物車
    elif ctype == 'update': 
        n = 0
        for unit in cartlist:
            unit[2] = request.POST.get('qty'+str(n),'1') #取得數量,'qty'是數量的意思
            unit[3] = str(int(unit[1])*int(unit[2]))  #總價
            n += 1
            request.session['cartlist'] = cartlist #將購物車內容存入session
            return redirect('/cart/')


    elif ctype == 'empty' : #清空購物車
        cartlist = list()
        request.session['cartlist'] = cartlist #將購物車內容存入session
        return redirect('/cart/')

    elif ctype == 'remove': #刪除購物車中的某一項商品
        del cartlist[int(productid)] #刪除商品編號
        request.session['cartlist'] = cartlist #將購物車內容存入session
        return redirect('/cart/')


def cartorder(request): #結帳--這邊要存資料庫 

    if request.session.get('Ulogined',False):   #若使用者已經登入時,就跳轉到customer.html
        global cartlist,customname,customphone,customaddress,customemail
        cart = cartlist
        total = 0
        for unit in cartlist:
            total += int(unit[3]) #每一項的價格加總
        grandtotal = total + 60 # 每一項的價格加總+60
        name = customname 		# 客戶名稱
        photo = customphone		# 客戶電話
        address = customaddress # 客戶地址
        email = customemail		# 客戶信箱
        return render(request,'cartorder.html',locals()) #全部回傳到'cartorder.html'
    else:                            
        return redirect('/login/')  #若使用者未登入時,就跳轉到login

    #global cartlist,customname,customphone,customaddress,customemail
	#allcart = cartlist
	#total = 0
	#for unit in cartlist:
	#	total += int(unit[3])

	#grandtotal = total + 60
	#name = customname
	#photo = customphone
	#address = customaddress
	#email = customemail
	#return render(request,'cartorder.html',locals())


	


def cartok(request): #最後確認買單
	global cartlist,customname,customphone,customaddress,customemail
	total = 0
	for unit in cartlist:
		total += int(unit[3])

	grandtotal = total + 60

	customname = request.POST.get('CuName','')
	customphone = request.POST.get('CuPhoto','')
	customaddress = request.POST.get('CuAddr','')
	customemail = request.POST.get('CuEmail','')
	payType = request.POST.get('payType','')
	#寫入資料庫------

	#與models.py 名稱相對應(明細)
	unitorder = models.OrderModel.objects.create(subtotal=total,shipping=60,grandtotal=grandtotal,
		customname=customname,customemail=customemail, 
		customphone=customphone,customaddress=customaddress,paytype=payType) #建立訂單
	for  unit in cartlist: #買了那些東西的明細
		total = int(unit[1])*int(unit[2]) #int(unit[1])金額*int(unit[2])數量, #dorder=unitorder 關聯式,訂單刪除跟著刪除
		unitdetail = models.DetailModel.objects.create(dorder=unitorder,pname=unit[0],
			unitprice=unit[1],quantity=unit[2],dtotal=total)



	orderid = unitorder.id #取得訂單編號

	name = unitorder.customname #取得購買者姓名
	email = unitorder.customemail #取得購買者信箱

	cartlist = list() #取得訂單編號後,購物車要變成空車
	request.session['cartlist'] =cartlist #購物車要變成空車
	return render(request,'cartok.html',locals()) #回傳 下定成功	


def cartordercheck(request): #查詢訂單
	orderid = request.GET.get('orderid','') #取得訂單編號
	customemail = request.GET.get('customemail','')#取得使用者信箱

	if orderid == '' and customemail =='':
		firstsearch = 1 #視為第一次查詢
	else:
		 order = models.OrderModel.objects.filter(id=orderid).first() #first() 抓取第一筆
		 if order == None or order.customemail != customemail: #
		 	notfound = 1
		 else:
		 	#details 明細
		 	details = models.DetailModel.objects.filter(dorder=order)


	return render(request,"cartordercheck.html",locals()) #回傳cartordercheck.html



def shopping(request):
    
    order_params = {
        'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'StoreID': '',
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'PaymentType': 'aio',
        'TotalAmount': 2000,
        'TradeDesc': '訂單測試',
        'ItemName': '商品1#商品2',
        'ReturnURL': 'https://www.ecpay.com.tw/return_url.php',
        'ChoosePayment': 'Credit',
        'ClientBackURL': 'https://www.ecpay.com.tw/client_back_url.php',
        'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
        'Remark': '交易備註',
        'ChooseSubPayment': '',
        'OrderResultURL': 'https://www.ecpay.com.tw/order_result_url.php',
        'NeedExtraPaidInfo': 'Y',
        'DeviceSource': '',
        'IgnorePayment': '',
        'PlatformID': '',
        'InvoiceMark': 'N',
        'CustomField1': '',
        'CustomField2': '',
        'CustomField3': '',
        'CustomField4': '',
        'EncryptType': 1,
    }
    
    extend_params_1 = {
        'BindingCard': 0,
        'MerchantMemberID': '',
    }
    
    extend_params_2 = {
        'Redeem': 'N',
        'UnionPay': 0,
    }
    
    inv_params = {
        # 'RelateNumber': 'Tea0001', # 特店自訂編號
        # 'CustomerID': 'TEA_0000001', # 客戶編號
        # 'CustomerIdentifier': '53348111', # 統一編號
        # 'CustomerName': '客戶名稱',
        # 'CustomerAddr': '客戶地址',
        # 'CustomerPhone': '0912345678', # 客戶手機號碼
        # 'CustomerEmail': 'abc@ecpay.com.tw',
        # 'ClearanceMark': '2', # 通關方式
        # 'TaxType': '1', # 課稅類別
        # 'CarruerType': '', # 載具類別
        # 'CarruerNum': '', # 載具編號
        # 'Donation': '1', # 捐贈註記
        # 'LoveCode': '168001', # 捐贈碼
        # 'Print': '1',
        # 'InvoiceItemName': '測試商品1|測試商品2',
        # 'InvoiceItemCount': '2|3',
        # 'InvoiceItemWord': '個|包',
        # 'InvoiceItemPrice': '35|10',
        # 'InvoiceItemTaxType': '1|1',
        # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
        # 'DelayDay': '0', # 延遲天數
        # 'InvType': '07', # 字軌類別
    }
    
    # 建立實體
    ecpay_payment_sdk = module.ECPayPaymentSdk(
        MerchantID='2000132',
        HashKey='5294y06JbISpM5x9',
        HashIV='v77hoKGq4kWxNNIS'
    )
    
    # 合併延伸參數
    order_params.update(extend_params_1)
    order_params.update(extend_params_2)
    
    # 合併發票參數
    order_params.update(inv_params)
    
    try:
        # 產生綠界訂單所需參數
        final_order_params = ecpay_payment_sdk.create_order(order_params)
    
        # 產生 html 的 form 格式
        action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
        # action_url = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5' # 正式環境
        html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
        return render(request,"buy.html",locals())
    except Exception as error:
        print('An exception happened: ' + str(error))    



