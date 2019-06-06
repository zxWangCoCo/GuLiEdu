from django import forms
from .models import UserAsk
from utils.RegexpUtil import RegexpUtil

class UserAskForms(forms.ModelForm):
    # 直接使用model中的验证规则
    class Meta:
        model = UserAsk
        # 如果用到部分字段
        fields = ['name','phone','course']
        # 如果用到所有字段
        #fields = '__all__'
        # 除了哪个字段
        #exclude = ['add_time']

    # 验证手机号(必须是clean开头)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        r = RegexpUtil.check_phone(phone=phone)
        if r:
            return phone
        else:
            raise forms.ValidationError('手机号码不合法')


