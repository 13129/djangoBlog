from django.urls import re_path,path,include
from rest_framework.routers import DefaultRouter
from users.views import UserProfileViewSits



router=DefaultRouter()
router.register(r'users',UserProfileViewSits,basename = 'users')


urlpatterns=[
	re_path(r'',include(router.urls)),
]

