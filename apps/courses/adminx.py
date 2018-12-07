import xadmin

from .models import CourseInfo,LessonInfo,videoInfo,SourceInfo

########################################课程表###########################################
class CourseInfoXadmin(object):
    list_display = ['image', 'name', 'study_time', 'study_num','leave','love_num','click_num','desc','detail','category','course_notice','course_need','teacher_tell','orgInfo','teacherIfo','add_time']

    search_fields = ['name', 'study_time', 'study_num', 'leave', 'love_num', 'click_num', 'desc', 'detail',
                    'category', 'course_notice', 'course_need', 'teacher_tell', 'orgInfo', 'teacherIfo']

    list_filter = ['name', 'study_time', 'study_num', 'leave', 'love_num', 'click_num', 'desc', 'detail',
                    'category', 'course_notice', 'course_need', 'teacher_tell', 'orgInfo', 'teacherIfo']

    model_icon = 'fa fa-address-book'


class LessonInfoXadmin(object):

    list_display=['name','courseInfo','add_time']

    search_fields = ['name', 'courseInfo']

    list_filter = ['name', 'courseInfo']

    model_icon = 'fa fa-address-book'


class videoInfoXadmin(object):
    list_display = ['name', 'study_time', 'lessonInfo','url','add_time']

    search_fields = ['name', 'study_time', 'lessonInfo']

    list_filter = ['name', 'study_time', 'lessonInfo','add_time']

    model_icon = 'fa fa-address-book'


class SourceInfoXadmin(object):
    list_display =['name','down_load','courseInfo','add_time']

    search_fields = ['name','courseInfo']

    list_filter = ['name','courseInfo', 'add_time']

    model_icon = 'fa fa-address-book'


xadmin.site.register(CourseInfo,CourseInfoXadmin)
xadmin.site.register(LessonInfo,LessonInfoXadmin)
xadmin.site.register(videoInfo,videoInfoXadmin)
xadmin.site.register(SourceInfo,SourceInfoXadmin)
