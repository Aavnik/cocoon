import threading
from django.conf import settings
from django.core.mail import send_mail


class Send_mail(threading.Thread):

    def __init__(self, email, email_tok):
        self.email = email
        self.email_tok = email_tok
       
      
        threading.Thread.__init__(self)

    def run(self):
        try:
            subject = "Verification Link form Cocoon"
            message = f"Hi! there's Click the link to activate your account -  https://cocoons.herokuapp.com//account/verify-email{self.email_tok}"
            email_from = settings.EMAIL_HOST_USER
            print("Email send initiated")
            reply_to=[email_from],
            send_mail(subject , message ,email_from ,[self.email])
            print("Email has been Sent")
        except Exception as e:
            print(e)