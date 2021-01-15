from django.shortcuts import render
from studentsapp.models import student
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler

logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('fT3GyLnoLosi7YceTc9XgOK2zJh/RLnoSVBbHtOi5TMFAh8zS6xVlPqqqWV4c8QsrVEdAgpHvnnbKS+nuVNFxcvz1V5cHHYYuPvKRGtV518WeGcbhFmd1XJgV9DNcRlBHIeJewOqu3KPO6xVlUGnagdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8aa414aee6a24cfa9763474df4b5cb3e')

line_bot_api.push_message('Udb26d71aa0a3d9bf631d2897b5d6ad85', TextSendMessage(text='你可以開始了'))
