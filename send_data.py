import email
import smtplib
import os
from email import encoders
from email.mine.multipart import MINEMultipart
import mimetypes
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

def send_email():
    sender = 'v.maksimova@ptl.ru'
    password = 'NogtyNaNogah75'
    adress = 'tender@ptl.ru'
    server = smtplib.SMTP(host='smtp.ptl.ru', port=587)
    server.starttls()
    
    try:
        server.login(sender, password)
        msg = MINEMultipart()
        msg['From'] = sender
        msg['To'] = adress
        msg['Subject'] = f'Визуализация данных по запросу {file_title}'
        
        for file in os.listdir('doc_for_send'):
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)
            file_type, subtype = ftype.split('/')
            
            with open(f'doc_for_send/{file}', 'rb') as f:
                file = MIMEBase(file_type, subtype)
                file.set_payload(f.read())
                encoders.encode_base64(file)

        server.sendmail(sender, adress, msg.asstring())
        
        for file in os.listdir('doc_for_send'):
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f{file})
            os.remove(path)
            
        return 'Message send'
    
    except Exception as _ex:
        return f'{_ex}\nPlease, check your login or password!'
            

def main():
    print(send_mail)

if __name__ == '__main__':
    main()
    

