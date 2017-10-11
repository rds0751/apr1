from django.contrib import admin

# Register your models here.
from .models import message
from .models import call

class messageAdmin(admin.ModelAdmin):
	class Meta:
		Model = message
		admin.site.register(message)

class callAdmin(admin.ModelAdmin):
	class Meta:
		Model = call
		admin.site.register(call)
		