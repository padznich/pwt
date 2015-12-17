import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtp_obj.ehlo())

smtp_obj.starttls()

smtp_obj.login('padznich@yandex.ru', '{password}')

smtp_obj.sendmail('padznich@yandex.ru', 'slabkopg@gmail.com', 'Subject: Hello.\n\nHello out of Python! How are you??:). Email Bot.')

smtp_obj.quit()

'''
import urllib2
import urllib
api_key = 'YOUR_API_KEY'
phone = 'YOUR_PHONE'
text = u'Testing.'

encoded_text = urllib.urlencode( {"text": text.encode('utf-8') } )

url_template = 'http://sms.ru/sms/send?api_id=%(api_key)s&to=%(phone)s'
url = url_template % {"api_key": api_key, "phone": phone}



headers = {"Content-type":  "application/x-www-form-urlencoded"}

r = urllib2.Request(url, data=encoded_text, headers=headers)
u = urllib2.urlopen(r)
u.read()
'''