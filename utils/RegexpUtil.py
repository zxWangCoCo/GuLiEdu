import re


class RegexpUtil:

    '''
        验证手机号
    '''
    REGEX_MOBILE = r'^1[3-9]\d{9}$'

    @staticmethod
    def check_phone(*, phone):
        return re.compile(RegexpUtil.REGEX_MOBILE).match(phone)


if __name__ == '__main__':
    print(RegexpUtil.check_phone(phone='15866522833'))
