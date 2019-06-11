from django.shortcuts import render
from .models import OrgInfo, TeacherIfo, CityInfo
# 分页相关
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

# 获取org,city列表


def org_list(request):
    all_orgs = OrgInfo.objects.all()
    all_citys = CityInfo.objects.all()
    # 根据喜爱人数排序
    sort_orgs = all_orgs.order_by('-love_num')[:3]

    # 按照机构类别过滤
    cate = request.GET.get('cate', '')
    if cate:
        all_orgs = all_orgs.filter(category=cate)

    # 按照城市过滤
    cityid = request.GET.get('cityid', '')
    if cityid:
        all_orgs = all_orgs.filter(cityinfo_id=int(cityid))

    #根据学习人数和课程数排序
    sort = request.GET.get('sort','')
    if sort:
        all_orgs = all_orgs.order_by('-'+sort)

    # 分页代码
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_orgs, 3)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'orgs/org-list.html', {
        'all_orgs': all_orgs,
        'pages': pages,
        'all_citys': all_citys,
        'sort_orgs': sort_orgs,
        'cate': cate,
        'cityid': cityid,
        'sort': sort
    })

# org详情
def org_detail(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        return render(request, 'orgs/org-detail-homepage.html',{
            'org':org
        })

def org_detail_course(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        all_org = org.courseinfo_set.all()
        # 分页代码
        pagenum = request.GET.get('pagenum', '')
        pa = Paginator(all_org, 3)
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        return render(request, 'orgs/org-detail-course.html', {
            'org': org,
            'pages':pages
        })

def org_detail_desc(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        return render(request, 'orgs/org-detail-desc.html', {
            'org': org
        })

def org_detail_teacher(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        return render(request, 'orgs/org-detail-teachers.html', {
            'org': org
        })