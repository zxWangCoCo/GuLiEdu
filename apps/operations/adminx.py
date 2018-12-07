import xadmin
from .models import UserAsk,UserLove,UserCourse,UserComment,UserMessage
class UserAskXadmin(object):
    list_display = ['name', 'phone','course','add_time']

    search_fields = ['name', 'phone', 'course']

    list_filter = ['name', 'phone', 'course', 'add_time']

    model_icon = 'fa fa-telegram'

class UserLoveXadmin(object):
    list_display = ['love_man', 'love_id', 'love_type', 'love_status','add_time']

    search_fields = ['love_man', 'love_id', 'love_type', 'love_status', 'add_time']

    list_filter = ['love_man', 'love_id', 'love_type', 'love_status', 'add_time']

    model_icon = 'fa fa-telegram'


class UserCourseXadmin(object):
    list_display = ['study_man', 'study_course','add_time']

    search_fields = ['study_man', 'study_course']

    list_filter = ['study_man', 'study_course']

    model_icon = 'fa fa-telegram'


class UserCommentXadmin(object):

    list_display = ['comment_man', 'comment_course', 'comment_content','add_time']

    search_fields = ['comment_man', 'comment_course', 'comment_content']

    list_filter = ['comment_man', 'comment_course', 'comment_content']

    model_icon = 'fa fa-telegram'

class UserMessageXadmin(object):

    list_display = ['message_man', 'message_content', 'message_status', 'add_time']

    search_fields = ['message_man', 'message_content', 'message_status']

    list_filter = ['message_man', 'message_content', 'message_status']

    model_icon = 'fa fa-telegram'

xadmin.site.register(UserAsk,UserAskXadmin)
xadmin.site.register(UserLove,UserLoveXadmin)
xadmin.site.register(UserCourse,UserCourseXadmin)
xadmin.site.register(UserComment,UserCommentXadmin)
xadmin.site.register(UserMessage,UserMessageXadmin)