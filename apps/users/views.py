from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.
#跳转首页
def index(request):
    return render(request,'index.html')

def user_register(request):
    if request.method == 'GET':#get请求是跳页面
        return render(request,'register.html')
    else:#post请求提交
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.changed_data['email']
            password = user_register_form.changed_data['password']
