import requests as req
from bs4 import BeautifulSoup as bs
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "denemeyapcaz321@hotmail.com"
password = "deneme321"

receiver = "cevat.can.ayguler@hotmail.com"
subject = "Yeni Duyuru"
#---

url="https://erzurum.edu.tr/duyuru/index/1052/1/#gsc.tab=0"
r=req.get(url)
soup= bs(r.content,"lxml")
tablo= soup.find("div",attrs={"class":"list"}).select("div")
yazdir=""
a=0
tarih=""
while True:
    if(tarih!=tablo[0].text):
        yazdir+="---\tDUYURULAR\t---\n"
        for i in range(0,4):
            if (i%2==0):
                yazdir+=f"Tarih: {tablo[i].text}\n"
            else:
                line=tablo[i].text
                line=line.lstrip()
                line=line.rstrip()
                yazdir+=f"Konu: {line}\n{"-"*30}\n"
        tarih=tablo[0].text
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(yazdir, 'plain'))
        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.starttls()
            server.login(sender, password)
            print("Giriş başarılı")
            server.sendmail(sender, receiver, message.as_string())
            print("Gönderim tamamlandı")
            server.quit()
        except Exception as e:
            print("An error occurred:", str(e))
    else:
        pass
    time.sleep(10)