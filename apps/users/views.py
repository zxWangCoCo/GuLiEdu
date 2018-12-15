from django.db.models import Q
from django.shortcuts import render,redirect,reverse
from .forms import UserRegisterForm
from .models import UserProfile
# Create your views here.
#跳转首页
def index(request):
    return render(request,'index.html')

def user_register(request):
    if request.method == 'GET':#get请求是跳页面
        return render(request,'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request,'register.html',{'msg':'用户已经存在'})
            else:
                user = UserProfile()
                user.username = email
                user.email = email
                user.set_password(password)
                user.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {'user_register_form': user_register_form })