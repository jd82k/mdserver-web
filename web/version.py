# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# 版本信息
# ---------------------------------------------------------------------------------

# 应用程序版本号组件
APP_RELEASE = 0
APP_REVISION = 18
APP_SMALL_VERSION = 1

# 应用程序版本后缀，例如“beta1”、“dev”。通常为空字符串GA发布
APP_SUFFIX = ''


#不要改变！由组件构造的应用程序版本字符串
if not APP_SUFFIX:
    APP_VERSION = '%s.%s.%s' % (APP_RELEASE, APP_REVISION, APP_SMALL_VERSION)
else:
    APP_VERSION = '%s.%s.%s-%s' % (APP_RELEASE, APP_REVISION, APP_SMALL_VERSION, APP_SUFFIX)
