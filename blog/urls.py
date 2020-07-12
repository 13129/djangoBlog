from blog import views
from rest_framework.routers import DefaultRouter
from django.urls import re_path,include



router=DefaultRouter()
router.register(r'blog',views.BlogViewSit,basename = 'blog')
router.register(r'category',views.CategoryViewSit,basename = 'category')

urlpatterns=[
	re_path(r'^',include(router.urls)),
]