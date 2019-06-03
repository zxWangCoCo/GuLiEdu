
from django import forms
from captcha.fields import CaptchaField

class UserRegisterForm(forms.Form):
    #验证邮箱
    email = forms.EmailField(required=True)
    #密码
    password = forms.CharField(required=True,min_length=3,max_length=15,
                               error_messages={
                                   'required':'密码必须填写',
                                   'min_length':'密码必须大于3位',
                                   'max_length':'密码最长为15位'
                                    }
                               )
    # captcha邀请码
    captcha = CaptchaField()
class UserLoginForm(forms.Form):
    #验证邮箱
    email = forms.EmailField(required=True)
    #密码
    password = forms.CharField(required=True,min_length=3,max_length=15,
                               error_messages={
                                   'required':'密码必须填写',
                                   'min_length':'密码必须大于3位',
                                   'max_length':'密码最长为15位'
                                    }
                               )