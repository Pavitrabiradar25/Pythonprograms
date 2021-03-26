import smtplib

class SendEmail:
    def SendMail():
        sender_email = "pavitrabiradar25@gmail.com"
        password = "*********"
        subject = input('Subject?<user inputs  subject>:\t')
        body = input('Body?<user inputs a one line body>:')
        receiver_mail = input('Recipient?<user inputs the email address of the recipient>:')
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_mail,subject,body)
        print('Email sent!')

if __name__=='__main__':
     obj = SendEmail
     obj.SendMail()

