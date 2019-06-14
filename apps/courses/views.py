from django.shortcuts import render
from .models import CourseInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def course_list(request):

    #获取所有课程
    all_course = CourseInfo.objects.all()

    #获取推荐的(按时间倒序)
    recomend_courses = all_course.order_by('-add_time')[:3]

    sort = request.GET.get('sort','')
    if sort:
        all_course.order_by('-'+sort)

    # 分页代码
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_course, 3)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'courses/course-list.html',{
        'pages':pages,
        'recomend_courses':recomend_courses,
    })