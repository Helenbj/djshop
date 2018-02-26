# -*- coding: utf-8 -*-

# import module from django & wechat_sdk
# pip install django && pip install wechat_sdk first
from __future__ import absolute_import, unicode_literals
import os
import wechatpy
from wechatpy import WeChatClient
from wechatpy.utils import check_signature
from wechatpy.exceptions import (InvalidSignatureException,InvalidAppIdException,)
from wechatpy.replies import (TextReply,ImageReply,VoiceReply,VideoReply,MusicReply,ArticlesReply,create_reply)
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pprint
from wechat.models import DiscountInfo

TOKEN = 'djshop12345678'
AES_KEY = 'UXopYywGSIztPwbFAxUoaaKgXTVnJt2yJ03IwgZ2W9G'

# following 2 lines is for real wechat
# APPID = 'wx6afbeb015042cb99'
# AppSecret = '8af25faf494e7aa05ea5fd0ac70318d2'

# following 2 lines is for test wechat
APPID = 'wxf6f3d7c77d422668'
AppSecret = '4274d6c632443800e11ff36826761c03'

# pass csrf check
@csrf_exempt
def groupbuyPanel(request):
    infoset = DiscountInfo.objects.filter(category='团购网站')
    merchantset = DiscountInfo.objects.filter(category='团购网站').values('merchant').distinct()
    imgset = DiscountInfo.objects.filter(category='团购网站').values('imgurl').distinct()
    context = {
        'title':  'takeout',
	'infoset': infoset,
	'merchantset': merchantset,
        'imgset': imgset,
    }
    return render(request, 'wechat/groupbuyPanel.html', context)
@csrf_exempt
def takeoutPanel(request):
    infoset = DiscountInfo.objects.filter(category='外卖')
    merchantset = DiscountInfo.objects.filter(category='外卖').values('merchant').distinct()
    imgset = DiscountInfo.objects.filter(category='外卖').values('imgurl').distinct()
    context = {
        'title':  'takeout',
	'infoset': infoset,
	'merchantset': merchantset,
        'imgset': imgset,
    }
    return render(request, 'wechat/takeoutPanel.html', context)
@csrf_exempt
def moviePanel(request):
    infoset = DiscountInfo.objects.filter(category='电影票')
    merchantset = DiscountInfo.objects.filter(category='电影票').values('merchant').distinct()
    imgset = DiscountInfo.objects.filter(category='电影票').values('imgurl').distinct()
    context = {
        'title':  'takeout',
	'infoset': infoset,
	'merchantset': merchantset,
        'imgset': imgset,
    }
    return render(request, 'wechat/moviePanel.html', context)
@csrf_exempt
def carorderPanel(request):
    infoset = DiscountInfo.objects.filter(category='用车')
    merchantset = DiscountInfo.objects.filter(category='用车').values('merchant').distinct()
    imgset = DiscountInfo.objects.filter(category='用车').values('imgurl').distinct()
    context = {
        'title':  'takeout',
	'infoset': infoset,
	'merchantset': merchantset,
        'imgset': imgset,
    }
    return render(request, 'wechat/carorderPanel.html', context)

@csrf_exempt
def addMaterial(request):
    print("go into ajax addMaterial.")
    client = WeChatClient(APPID, AppSecret)
    openFile = open('/home/helen/projects/djshop/djshoproj/static/wechat/img/COACH_5.jpg', 'rb')
    materialType = 'image'
    response = client.material.add(materialType, openFile)	
    pprint.pprint(response)
    context = {
        "title":  'wechatpy.client.material.add',
        "media_id": response['media_id']
    }
    # pprint.pprint(material)
    return render(request, 'wechat/addMaterial.html', context)
    
@csrf_exempt
def createMenu(request):
    print("go into ajax createMenu.")
    client = WeChatClient(APPID, AppSecret)
    response = client.menu.create({
    "button":
    [
        {
            "name": "底价分类",
            "sub_button":
            [
                {
                     "type": "view",
                     "name": "团购",
                     "url": "http://39.106.98.42/djshop/wechat/groupbuyPanel"
                },
                {
                    "type": "view",
                    "name": "外卖",
                    "url": "http://39.106.98.42/djshop/wechat/takeoutPanel"
                },
                {
                     "type": "view",
                     "name": "约车",
                     "url": "http://39.106.98.42/djshop/wechat/carorderPanel"
                },
                {
                    "type": "view",
                    "name": "电影票",
                    "url": "http://39.106.98.42/djshop/wechat/moviePanel"
                },
            ]
        },
        {
            "name": "底价消息",
            "sub_button":
            [
                {
                    "type": "click",
                    "name": "省钱必看",
                    "key": "piggy"
                },
                {
                     "type": "click",
                     "name": "近期优惠",
                     "key": "jasper"
                },
            ]
        },
        {
            "type": "media_id",
            "name": "商务合作",
            "media_id": "Sf7M0xlLiNfkGlXla8hyVbx0TjvKPhxrs6ECOlDfmIs"
        }
    ]
    })
    pprint.pprint(response)
    context = {
        "title":  'wechatpy.client.api.WeChatMenu.create',
        "errcode": response['errcode'],
        "errmsg": response['errmsg']
    }
    # openFile = open('/home/helen/projects/djshop/djshoproj/static/wechat/img/COACH_1.jpg', 'rb')
    # material = client.material.add('image', openFile)	
    # pprint.pprint(material)
    return render(request, 'wechat/createMenu.html', context)

@csrf_exempt
def wechatHome(request):
    # get signature, timestamp and nonce
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    encrypt_type = request.GET.get('encrypt_type')
    msg_signature = request.GET.get('msg_signature')

    try:
        check_signature(TOKEN, signature, timestamp, nonce)
        if request.method == 'GET':
            response = request.GET.get('echostr')
            return HttpResponse(response, content_type="application/json")

	# POST request
        if encrypt_type != None:
            # encryption mode
            print("request is encrypt")
            from wechatpy.crypto import WeChatCrypto
            crypto = WeChatCrypto(TOKEN, AES_KEY, APPID)
            try:
                # now msg is xml
                msg = crypto.decrypt_message(
                   request.body,
                   msg_signature,
                   timestamp,
                   nonce
                )
            except (InvalidSignatureException, InvalidAppIdException):
                HttpResponseBadRequest("decrypt message error")
        else:
        	msg = request.body
        # plaintext mode
        print("before parse_message")
        pprint.pprint(msg)
        msg = wechatpy.parse_message(msg)
        print("after parse_message")
        pprint.pprint(msg)
        if msg.type == 'text':			# text message
            reply = TextReply(message=msg)
            reply.content = 'text reply'
        elif msg.type == 'image':
            reply = ImageReply(message=msg)
            reply.media_id = msg.media_id
        elif msg.type == 'voice':
            reply = VoiceReply(message=msg)
            reply.media_id = 'voice media id'
        elif msg.type == 'video':
            reply = VideoReply(message=msg)
            reply.media_id = 'video media id'
            reply.title = 'video title'
            reply.description = 'video description'
        elif msg.type == 'music':
            reply = MusicReply(message=msg)
            reply.thumb_media_id = 'thumb media id'
            reply.title = 'music title'
            reply.description = 'music description'
            reply.music_url = 'music url'
            reply.hq_music_url = 'hq music url'
        elif msg.type == 'news':
            reply = ArticlesReply(message=msg, articles=[
            {
                'title': u'标题1',
                'description': u'描述1',
                'url': u'http://www.qq.com',
            },
            ])
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return HttpResponse(reply.render(),content_type="application/json")
    except InvalidSignatureException as e:
        print("check_signature failed")
        HttpResponseBadRequest(e)
# END
