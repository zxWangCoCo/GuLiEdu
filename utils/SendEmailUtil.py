from users.models import EmailVerifyCode
from random import choice
from django.core.mail import send_mail
from GuliEdu.settings import EMAIL_FROM

class SendEmailUtil:

    @staticmethod
    def getRandomCode(codeLength):
        codeCourse = '1234567890qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM'
        code = ''
        for i in range(codeLength):
            str = choice(codeCourse)
            code += str
        return code

    @staticmethod
    def sendEmail(*,email,send_type):
        code = SendEmailUtil.getRandomCode(5)
        a = EmailVerifyCode()
        a.send_type = send_type
        a.email = email
        a.code = code
        a.save()
        recipient_list = [email]
        if send_type == 1:
            subject = '欢迎注册'
            message = '请点击以下链接进行激活,激活您的账号: \n http://127.0.0.1:8000/users/user_active/'+code
        # 发送邮件
        send_mail(subject=subject,message=message,from_email = EMAIL_FROM,recipient_list = recipient_list)