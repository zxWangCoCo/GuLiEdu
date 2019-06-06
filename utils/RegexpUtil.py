import re


class RegexpUtil:

    '''
        验证手机号
    '''
    REGEX_MOBILE = r'^1[3-9]\d{9}$'

    '''
        验证邮箱
    '''
    REGEX_EMAIL = r'^\w+@(\w+\.)+(com|cn|net|edu)$'

    @staticmethod
    def check_phone(*, phone):
        return re.compile(RegexpUtil.REGEX_MOBILE).match(phone)

    @staticmethod
    def check_email(*, email):
        return re.compile(RegexpUtil.REGEX_EMAIL).match(email)


if __name__ == '__main__':
    print('phone', RegexpUtil.check_phone(phone='15866522833'))
    print('email', RegexpUtil.check_email(email='443269741@qq.com'))
