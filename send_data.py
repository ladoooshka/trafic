
import smtplib
import os
from email import encoders
from email.mime.multipart import MIMEMultipart
import mimetypes
from email.mime.base import MIMEBase
from subprocess import Popen, PIPE

def send_email(file_title):
    sender = 'smtp.relay.ptl.ru'
    adress = 'tender@ptl.ru'
    server = smtplib.SMTP('relay.ptl.ru:25')
    server.starttls()
    
    try:
        from email.mime.text import MIMEText
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = adress
        msg['Subject'] = f'Визуализация данных по запросу {file_title}'
        p = Popen(['tendrftp', '-t', '-oi'], stdin=PIPE, universal_newlines=True)
        p.communicate(msg.as_string())

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
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{file}')
            os.remove(path)
            
        return 'Message send'
    
    except Exception as _ex:
        return f'{_ex}\nPlease, check your login or password!'
            

def main():
    send_email()

if __name__ == '__main__':
    main()
    

