from django.shortcuts import render
from .models import OrgInfo, TeacherIfo, CityInfo
from operations.models import UserLove
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
        lovestatus = False
        # 经过认证
        if request.user.is_authenticated():
            # 看看是否收藏
            love = UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus = True

        #返回收藏状态
        return render(request, 'orgs/org-detail-homepage.html',{
            'org':org,
            'lovestatus':lovestatus
        })

def org_detail_course(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        all_org = org.courseinfo_set.all()
        lovestatus = False
        # 经过认证
        if request.user.is_authenticated():
            # 看看是否收藏
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True
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
            'pages':pages,
            'lovestatus':lovestatus
        })

def org_detail_desc(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        # 经过认证
        if request.user.is_authenticated():
            # 看看是否收藏
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True
        return render(request, 'orgs/org-detail-desc.html', {
            'org': org,
            'lovestatus':lovestatus
        })

def org_detail_teacher(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        # 经过认证
        if request.user.is_authenticated():
            # 看看是否收藏
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True
        return render(request, 'orgs/org-detail-teachers.html', {
            'org': org,
            'lovestatus':lovestatus
        })

def teacher_list(request):

    teacher_list = TeacherIfo.objects.all()

    sort = request.GET.get('sort','')
    if sort:
        teacher_list = teacher_list.order_by('-'+'click_num')

    # 分页代码
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(teacher_list, 5)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    order_teacher_list = TeacherIfo.objects.all().order_by('-'+'love_num')[:5]

    return render(request,'teacher/teachers-list.html',{
        'pages':pages,
        'order_teacher_list':order_teacher_list,
        'sort':sort
    })