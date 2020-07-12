from rest_framework import viewsets,mixins
from rest_framework.decorators import action
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from blog.models import  Tag,Category,Blog
from blog.serializers import BlogSerializer,CategorySerializer,CategorySimpleSerializer,TagSerializer

# Create your views here.

class BlogViewSit(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
	"""
		查询一个和多个.list(),.retrieve()]
		重写retrieve()方法，实现文章访问量增加
	"""
	serializer_class = BlogSerializer
	queryset = Blog.objects.all()
	def retrieve(self, request, *args, **kwargs):
		instance=self.get_object()
		instance.increase_views()
		serializer=self.get_serializer(instance)
		return Response(serializer.data)


class CategoryViewSit(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
	'''

	'''
	queryset = Category.objects.all()
	def get_serializer_class(self):
		if self.action=='list':
			return CategorySimpleSerializer
		else:
			return CategorySerializer









