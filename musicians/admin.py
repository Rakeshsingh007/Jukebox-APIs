from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import Musicians



class MusiciansAdmin(admin.ModelAdmin):
	ordering = ('id',)
	list_per_page = 50
	list_display =  ('musicians_name','musicians_type')
	search_fields = ('musicians_name',)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Musicians,MusiciansAdmin)