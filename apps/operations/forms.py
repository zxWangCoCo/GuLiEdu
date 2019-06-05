from django import forms
from .models import UserAsk

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
