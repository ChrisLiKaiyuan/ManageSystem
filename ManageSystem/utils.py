from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, status
from rest_framework.pagination import PageNumberPagination
from django.utils.encoding import force_text

ERROR_MESSAGE = dict(
    # register
    username_unique="用户名已存在",
    username_null="用户名不能为空值",
    email_unique="该邮箱已被注册",
    email_null="邮箱不能为空值",
    invite_code_error="邀请码错误",
    password_confirmed_error="两次输入密码不一致",
    # login
    wrong_username_password="错误的用户名或密码",
    # change_password
    wrong_old_password="错误的当前密码",
    # logout
    login_without_logout="请先退出当前用户再登录",
    # create_information
    name_error="姓名不正确",
    sex_error="性别不正确",
    number_format_error="学号格式不正确",
    qq_format_error="qq号格式不正确",
    intension_error="意愿格式不正确",
    phone_format_error="手机号码格式不正确",
    # captcha
    no_captcha="验证码不能为空",
    captcha_error="验证码错误",
    code_too_long="代码长度超出此限制",
    id_error="id不符合要求",
    code_cannot_be_null="提交内容不能为空",
    cas_login_failed="CAS登录失败，请重试"
)


# 自定义错误类
class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Request Bad.'

    def __init__(self, detail, field, status_code=None):
        if status_code is not None: self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(response.data, dict):
        data = response.data.copy()
        error_msg = {field: details[0] if isinstance(details, list) else details for field, details in data.items()}
        response.data.clear()
        response.data['status'] = "error"
        response.data['error_msg'] = error_msg
    return response


# 分页类

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100
