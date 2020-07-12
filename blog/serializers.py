from rest_framework import serializers
from blog.models import Blog,Tag,Category
from users.serializers import UserProfileSerializer

class TagSerializer(serializers.ModelSerializer):
	"""
		博客标签序列化
	"""
	class Meta:
		model=Tag
		fields=('id','name',)



class BlogSerializer(serializers.ModelSerializer):
	'''
	博客信息序列化
	'''
	name=serializers.CharField(source = 'name.nickname',read_only = True)
	tags=serializers.CharField(source = 'tags_list',read_only = True)
	category=serializers.CharField(source = 'category.name',read_only = True)
	class Meta:
		model=Blog
		fields=('id','name','title','content','create_time','update_time','views','category','tags')
		read_only_fields=('id','name','title','content','create_time','update_time','views','category','tags')
	#动态修改字段
	def __init__(self, *args, **kwargs):
		remove_fields = kwargs.pop('remove_fields', None)
		super(BlogSerializer, self).__init__(*args, **kwargs)
		if remove_fields:
			for field_name in remove_fields:
				self.fields.pop(field_name)

#自定义创建序列化
# 	def create(self, validated_data):
# #
# # 		for i in validated_data:
# # 			print(i.id)
# # 		return validated_data

class CategorySerializer(serializers.ModelSerializer):
	"""
		博客标签序列化
	"""
	cate_blog=serializers.SerializerMethodField()

	def get_cate_blog(self,obj):
		blog=Blog.objects.filter(category = obj.id)

		if blog is not None and len(blog)>0:
			return BlogSerializer(blog,many = True,remove_fields = ['update_time','content',]).data
		else:
			return ''

	class Meta:
		model=Category
		fields=('id','name','cate_blog',)



class CategorySimpleSerializer(serializers.ModelSerializer):

	class Meta:
		model=Category
		fields=('id','name',)





