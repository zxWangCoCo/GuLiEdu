from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

from .forms import UserRegisterForm,UserLoginForm
from .models import UserProfile,EmailVerifyCode
from django.contrib.auth import authenticate,login,logout
from utils.SendEmailUtil import SendEmailUtil
from .models import EmailVerifyCode
# Create your views here.
#跳转首页
def index(request):
    return render(request,'index.html')

############################用户注册##############################################################
def user_register(request):
    if request.method == 'GET':#get请求是跳页面
        #这里实例化form，不是为了验证,而是为了验证验证码
        user_register_form = UserRegisterForm()
        return render(request,'users/register.html',{
            'user_register_form':user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request,'users/register.html',{'msg':'用户已经存在'})
            else:
                user = UserProfile()
                user.username = email
                user.email = email
                user.set_password(password)
                user.save()
                #发送邮件
                SendEmailUtil.sendEmail(email = email,send_type = 1)
                return HttpResponse('请尽快激活您的邮箱，否则无法登陆。')
        else:
            return render(request, 'users/register.html', {'user_register_form': user_register_form })
############################用户注册##############################################################

############################用户登录##############################################################
def user_login(request):
    if request.method == 'GET':
        return render(request,'users/login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']

            #查询是否有
            user = authenticate(username=email,password=password)
            if user:
                if user.is_start:
                    login(request,user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('请去你的邮箱激活，否则无法登陆')
            else:
                return render(request,'users/login.html',{
                    'msg':'邮箱或者密码有误'
                })
        else:
            return render(request, 'users/login.html', {'user_login_form': user_login_form})

##################################退出############################################################
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

def user_active(request,code):
    #获取code
    if code:
        # 根据code获取Email列表
        email_var_list = EmailVerifyCode.objects.filter(code=code)
        if email_var_list:
            # 获取第一个
            email_var = email_var_list[0]
            # 获取email
            email = email_var.email
            # 根据email获取用户
            user_list = UserProfile.objects.filter(username=email)
            if user_list:
                user = user_list[0]
                # 更改用户状态为激活状态
                user.is_start = True
                user.save()
                return redirect(reverse('users:user_login'))
            else:
                pass
        else:
            pass
    else:
        pass