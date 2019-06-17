from .forms import UserAskForms
from django.http import JsonResponse
from .models import UserLove

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

# 会员收藏机构
def user_love(request):
    love_id = request.GET.get('love_id','')
    love_type = request.GET.get('love_type','')
    # 验证参数
    if love_id and love_type:
        # 查询是否收藏过 request.user 在登录的时候已经存了用户信息
        love = UserLove.objects.filter(love_id=int(love_id),love_type=int(love_type),love_man=request.user)
        # 如果有过收藏
        if love:
            # 状态为取消收藏 修改状态为收藏
            if love[0].love_status:
                love[0].love_status = False
                love[0].save()
                return JsonResponse({'status':'ok','msg':'收藏'})
            else:
                # 如果收藏过了 但状态是取消收藏 修改状态(收藏)
                love[0].love_status = True
                love[0].save()
                return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
        else:
            # 如果没有收藏记录,直接收藏,状态为收藏
            a = UserLove()
            a.love_man = request.user
            a.love_id = int(love_id)
            a.love_type = int(love_type)
            a.love_status = True
            a.save()
            return JsonResponse({'status': 'ok', 'msg': '收藏'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '收藏失败'})