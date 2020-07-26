# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re
import re, random

tkr =["jmkfd[esaq]","wscq[fcaqw]","wxca[cxa]","1exaw2[s2qw]","wq2we[cwq2]","xcqaw[caw2]","w212sa[wsc]","cawq1[1fsa]","fuck[line]","3wqwd[cxaw]","wcx2[caw]","cxzw[45xca]"]

class Config(object):
    Q_HOST = "ga2"
    #Q_HOST = "ga2"
    DOMAIN = "line.naver.jp"
    #DOMAIN = "line-apps-beta.com"
    #Q_HOST = "legy-beta"
    LINE_HOST_DOMAIN            = 'https://%s.%s' % (Q_HOST, DOMAIN) #ga2, #gfp, #gd2x
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://%s.%s/mh/api' % (Q_HOST, DOMAIN)
    LINE_TIMELINE_MH            = 'https://%s.%s/mh' % (Q_HOST, DOMAIN)
    LINE_LIFF_SEND              = 'https://api.line.me/message/v3/share'
    LINE_PERMISSION_API         = 'https://access.line.me/dialog/api/permissions'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4' #F
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'

    CHANNEL_ID = {
        'HELLO_WORLD': '1602289196',
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '10.1.1',
        'IOS': '10.1.1',
        'ANDROIDLITE': '2.12.0',
        'DESKTOPWIN': '5.21.3',
        'DESKTOPMAC': '5.21.3',
        'IOSIPAD': '10.1.1',
        'CHROMEOS': '2.3.3',
        'DEFAULT': '10.1.1'
    }

    SYSTEM_VERSION = {
        'ANDROID': '10.0',
        'IOS': '13.3.1',
        'ANDROIDLITE': '10.0',
        'DESKTOPWIN': '10.0',
        'DESKTOPMAC': '10.15.1',
        'IOSIPAD': '13.3.1',
        'CHROMEOS': '79.0',
        'DEFAULT': '10.0'
    }

    APP_TYPE    = 'DESKTOPWIN'
    APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = random.choice(tkr)
    SYSTEM_VER  = SYSTEM_VERSION[APP_TYPE] if APP_TYPE in SYSTEM_VERSION else SYSTEM_VERSION['DEFAULT']
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    URL_REGEX   = re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    MID_REGEX   = re.compile(r'u\w{32}')
    GID_REGEX   = re.compile(r'c\w{32}')
    RID_REGEX   = re.compile(r'r\w{32}')
    ALLIDS_REGEX= re.compile(r'(?:u\w{32}|c\w{32}|r\w{32})')

    def __init__(self, appType=None):
        if appType:
            self.APP_TYPE = appType
            self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER
