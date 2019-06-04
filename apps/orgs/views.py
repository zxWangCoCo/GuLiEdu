from django.shortcuts import render
from .models import OrgInfo, TeacherIfo, CityInfo
# Create your views here.

# 获取org,city列表
def org_list(request):
    all_orgs = OrgInfo.objects.all()
    all_citys = CityInfo.objects.all()
    return render(request, 'org-list.html', {
        'all_orgs': all_orgs,
        'all_citys': all_citys,
    })
