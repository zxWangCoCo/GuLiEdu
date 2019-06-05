from .forms import UserAskForms
from django.http import JsonResponse

def user_ask(request):
    user_ask_form = UserAskForms(request.POST)
    # 如果合法
    if user_ask_form.is_valid():
        # 直接保存,否则还要使用Model保存
        user_ask_form
        user_ask_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'咨询成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '咨询失败'})
