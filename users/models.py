from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
from django.core.files.base import ContentFile

import os
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .mugshot import Avatar



def user_mugshot_path(instance,filename):
	return os.path.join('mugshots',instance.username,filename)


class UserProfile(AbstractUser):
	"""
	用户模型自定义
	"""
	last_login_ip = models.GenericIPAddressField(
		"最近一次登录",
		unpack_ipv4=True,
		blank=True,
		null=True
	)
	register_ip = models.GenericIPAddressField("注册IP",unpack_ipv4=True,blank=True,null=True)
	nickname = models.CharField("昵称",max_length=50,unique=True)#unique保持唯一性
	mugshot = models.ImageField("头像",upload_to=user_mugshot_path)#头像路径保存
	mugshot_thumbnail = ImageSpecField(source='mugshot',
	                                   processors=[ResizeToFill(100,100)],
									   format='JPEG',
	                                   options={'quality':60})


	class Meta:
		swappable='AUTH_USER_MODEL'
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		ordering = ['-id']


	def __str__(self):
		return self.username


	def save(self, *args, **kwargs):
		if not self.mugshot:
			avatar=Avatar(rows=10,columns=10)
			img_byte_array=avatar.get_image(
				string = self.username,
				height = 480,
				width = 480,
				pad = 10)
			self.mugshot.save('default_mugshot.png',ContentFile(img_byte_array),save = False)
		if not self.pk and not self.nickname:
			self.nickname=self.username
		super(UserProfile,self).save(*args,**kwargs)

from django.conf import settings
from ipware import get_client_ip

def get_ip_address_from_request(request):
	'''
		django-ipware模块--返回客户端真实IP地址
		返回request中的IP地址
	'''
	ip,is_routable=get_client_ip(request)
	if settings.DEBUG:
		return ip
	else:
		if ip is not None and is_routable:
			return ip
	return None

def update_last_login_ip(sender,user,request,**kwargs):
	'''更新最后一次登录的地址'''
	ip=get_ip_address_from_request(request)
	if ip:
		user.last_login_ip=ip
		user.save()

user_logged_in.connect(update_last_login_ip)#登录成功时发送信号