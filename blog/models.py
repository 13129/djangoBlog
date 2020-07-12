from django.conf import settings
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
"""数据库表"""


# 分类
class Category (models.Model):
	name = models.CharField (verbose_name = '文章类别', max_length = 20)
	class Meta:
		verbose_name = '文章类别'
		verbose_name_plural = verbose_name
	def __str__ (self):
		return self.name



# 轮播图


# 文章标签
class Tag (models.Model):
	name = models.CharField (verbose_name = '文章标签', max_length = 20)
	class Meta:
		verbose_name = '文章标签'
		verbose_name_plural = verbose_name
	def __str__ (self):
		return self.name



# 博客
class Blog (models.Model):
	name = models.ForeignKey (settings.AUTH_USER_MODEL, verbose_name ='作者', on_delete = models.CASCADE)
	title = models.CharField (verbose_name = '标题', max_length = 100)
	content=RichTextField(verbose_name = '正文',config_name = 'my_config')
	create_time = models.DateTimeField (verbose_name = '创建时间', default = timezone.now)
	update_time = models.DateTimeField (verbose_name = '修改时间', auto_now = True)
	views = models.IntegerField(verbose_name = '阅读量', default = 0)
	category = models.ForeignKey (Category,verbose_name = '文章类别',related_name = 'cate_blog', on_delete = models.DO_NOTHING)
	tags = models.ManyToManyField (Tag, verbose_name = '文章标签', )  # 多对多的外键关系


	class Meta:
		verbose_name = '我的博客'
		verbose_name_plural = verbose_name
		ordering = ['-update_time']

	def increase_views(self):#增加模型方法
		self.views+=1
		self.save(update_fields = ['views',])

	def tags_list(self):#后台显示标签
		return ','.join([tag.name for tag in self.tags.all()])

	def __str__ (self):
		return self.title