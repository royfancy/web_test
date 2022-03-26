from django.db import models

# Create your models here.
class  OrderModel(models.Model): #訂單
	subtotal = models.IntegerField(default=0) #購物金額 (default=0) 預設0  
	shipping = models.IntegerField(default=0) #運費
	grandtotal = models.IntegerField(default=0) #總計=購物金額+運費
	customname = models.CharField(max_length=100) #客戶名稱
	customemail = models.CharField(max_length=100) #客戶信箱
	customphone = models.CharField(max_length=20) #客戶電話
	customaddress = models.CharField(max_length=200) #客戶地址
	paytype = models.CharField(max_length=30) #付款方式
	create_date = models.DateTimeField(auto_now_add=True) #訂單建立時間

	def __str__(self):  #回傳
		return self.customname #回傳客戶名

class  DetailModel(models.Model): #訂單明細
	dorder = models.ForeignKey('OrderModel',on_delete=models.CASCADE)
		                      #外來鍵('OrderModel':類別名稱,on_delete=models.CASCADE:當類別被刪除,相對要被刪除)
		                      #django 裡面 稱 多對一
	pname = models.CharField(max_length=100)  #商品名稱
	unitprice = models.IntegerField(default=0)#價格
	quantity = models.IntegerField(default=0) #數量
	dtotal = models.IntegerField(default=0)   #
	def __str__(self): #回傳
		return self.pname	#pname商品名稱                  




