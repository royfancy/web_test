from django.shortcuts import render

# Create your views here.
from email.mime.text import MIMEText  #email.mime.text:信件模組
from smtplib import SMTP,SMTPAuthenticationError,SMTPException

def sendMail(request):
	smtp = "smtp.gmail.com:587"#Gmail 主機位置
	account = "owls4112@gmail.com" #Gmail 帳號
	password = "Mistake19910607"   #Gmail 密碼

	content = "感業您的訂購!"
	msg = MIMEText(content) #郵件內容方式 寄出

	msg['Subject'] = '叮叮叮叮購物城' #郵件主旨
	mailto = "owls4112@gmail.com" #收件者

	#多人寄信方式
	#mailto = ['owls4112@gmail.com','owls4113@gmail.com']


	#做連線
	server = SMTP(smtp) #建立SMTP 連線

	server.ehlo() #跟主機溝通用

	server.starttls() #使用TTLS安全認證

	try:
		server.login(account.password) #登入用
		server.sendmail(account,mailto,msg.as_string())#寄信用


		sendMsg = '郵件飛走了' #丟出訊息

	except SMTPAuthenticationError:
		sendMsg = '無法登入'

	except :
		sendMsg = '郵件飛不出去'

	server.quit() #關閉連線

	return render(request,"sendMailPage.html",locals())















