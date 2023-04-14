from string import Template
from datetime import datetime
from dados_email import meu_email,minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


with open ('template.html','r') as html:
    template= Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg=template.substitute(nome='Luiz Otávio',data=data_atual)
    
msg = MIMEMultipart()
msg['from']='Júlio César Barbosa'
msg['to'] = meu_email
msg['subject'] = 'atenção, este é um e-mail de testes.'
corpo = MIMEText(corpo_msg,'html')
msg.attach(corpo)   
with open('imagem.png','rb') as img:
    img=MIMEImage(img.read())
    msg.attach(img)
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email,minha_senha)
    smtp.send_message(msg)
    print('email enviado com sucesso')