from django.contrib import admin
from users.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['nickname','email','password','register_ip','last_login_ip']
admin.site.register(UserProfile,UserProfileAdmin)
