from django.shortcuts import render
from .models import CourseInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from operations.models import UserLove,UserCourse
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

def course_detail(request,id):
    if id:
        course = CourseInfo.objects.filter(id=int(id))[0]
        # 获取相关课程 exclude()排除自己
        re_course = CourseInfo.objects.filter(category=course.category).exclude(id=int(course.id))[:2]
        lovecourse = False
        loveorg = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_id=int(id),love_type=2,love_status=True,love_man=request.user)
            if love:
                lovecourse = True
            love = UserLove.objects.filter(love_id=course.orgInfo.id, love_type=1, love_status=True, love_man=request.user)
            if love:
                loveorg = True
        return  render(request,'courses/course-detail.html',{
            'course':course,
            're_course':re_course,
            'lovecourse':lovecourse,
            'loveorg':loveorg
        })

def course_video(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(id=int(course_id))[0]
        #当用户点击学习时,代表该用户学习了该课程，如果没有学习则加上学习操作
        usercourse_list = UserCourse.objects.filter(study_course=course,study_man=request.user)
        if not usercourse_list:
            a = UserCourse()
            a.study_man = request.user
            a.study_course = course
            a.save()

        #学过该课程的学生还学过什么
        usercourse_list = UserCourse.objects.filter(study_course=course)
        #列表生成式
        user_list = [usercourse.study_man for usercourse in usercourse_list]
        #__in:在哪个范围内
        # exclude去除...
        usercourse_list = UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        # 拿到课程
        # set()用于去重
        course_list = list(set([usercourse.study_course for usercourse in usercourse_list]))

        return render(request,'courses/course-video.html',{
            'course':course,
            'course_list':course_list
        })

def course_comment(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(course_id=int(course_id))[0]

        course = CourseInfo.objects.filter(id=int(course_id))[0]
        # 当用户点击学习时,代表该用户学习了该课程，如果没有学习则加上学习操作
        usercourse_list = UserCourse.objects.filter(study_course=course, study_man=request.user)
        if not usercourse_list:
            a = UserCourse()
            a.study_man = request.user
            a.study_course = course
            a.save()

        # 学过该课程的学生还学过什么
        usercourse_list = UserCourse.objects.filter(study_course=course)
        # 列表生成式
        user_list = [usercourse.study_man for usercourse in usercourse_list]
        # __in:在哪个范围内
        # exclude去除...
        usercourse_list = UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        # 拿到课程
        # set()用于去重
        course_list = list(set([usercourse.study_course for usercourse in usercourse_list]))

        return render(request, 'courses/course-comment.html', {
            'course': course,
            'course_list':course_list
        })

