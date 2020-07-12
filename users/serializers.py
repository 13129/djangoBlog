from rest_framework import serializers
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
	'''用户详细信息序列化器'''

	class Meta:
		model=UserProfile
		fields=('id','username','nickname','email','date_joined',
		        'register_ip','last_login_ip','is_superuser','is_staff',)

		read_only_fields = ('id','username','date_joined',
		        'register_ip','last_login_ip','is_superuser','is_staff',)