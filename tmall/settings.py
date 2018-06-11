import os
import sys

# 目录的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 使用自定义的apps
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'ext_apps'))
# 加密的秘钥  例如 自带用户密码加密
SECRET_KEY = 'l3(wxpu5lctbe*h@l=j-u=3t$f@s+f2rj_bdy+gurpb&p)1%m)'
# 开发的时候设置True,如果是部署到服务器,需要设置False
DEBUG = True
# 访问的ip地址, 部署到服务器的的时候使用 "*"
ALLOWED_HOSTS = []
#  自定义的APPS
CUSTOM_APPS = [
    'apps.shop',
    'apps.car',
    'apps.account',
]

# 扩展的第三方库
EXT_APPS = [
    # 必须
    'xadmin',
    'crispy_forms',
    # 可选
    # 扩展主题包
    'reversion'
]

# 系统默认的app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 注册 application
INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS
# 中间件注册
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 项目的根urls
ROOT_URLCONF = 'tmall.urls'
# 模板相关的配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.shop.global_var.get_url',
            ],
        },
    },
]
# 部署
WSGI_APPLICATION = 'tmall.wsgi.application'
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tmall',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
# django 认证系统
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# 语言
LANGUAGE_CODE = 'zh-hans'
# 使用上海时区
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# 通过浏览器地址栏访问静态资源的根路径
STATIC_URL = '/static/'
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 指定项目静态文件根目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/shop/static'),
)
# 上传文件访问根路径
MEDIA_URL = '/media/'
# 指定上传目录的根路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 如果在测试环境下,能够访问到我的上传的资源,需要在根目录下urls.py中配置
# 'http://127.0.0.1:8000/static/
TEMP_STATIC_URL = 'http://127.0.0.1:8000' + STATIC_URL
TEMP_MEDIA_URL = 'http://127.0.0.1:8000' + MEDIA_URL
