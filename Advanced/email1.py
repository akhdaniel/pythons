import smtplib
sender = "info@vitraining.com"
receivers = ['donald@trupm.com','ade@ade.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message. """

try:
	smtpObj = smtplib.SMTP('192.168.2.106') 
	smtpObj.sendmail(sender, receivers, message) 
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"
