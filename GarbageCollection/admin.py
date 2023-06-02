from django.contrib import admin
from . models import Collection, PostNews, CreatePickup, Waste, Header, Goal, PostEvent, FooterBusinessHours, UserInfo,Footer
# Register your models here.


admin.site.site_header = "CleanSweep Admin"
admin.site.site_title = "CleanSweep Admin Portal"
admin.site.index_title = "Welcome to CleanSweep Admin"

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('route', 'city', 'street', 'schedule', 'route_image', 'route_link',
                    'type', 'type_2', 'type_3', 'type_4', 'type_5')


class PostNewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'post_date', 'post_image')


class PickupAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'city', 'barangay', 'street', 'building', 'house_no', 'type', 'date', 'last_updated')
    list_display = ('status', 'user', 'city', 'barangay', 'type', 'date', 'comment_request', 'building', 'last_updated')
    ordering = ('date',)
    list_filter = ('status',)


class WasteAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'post_image')


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('text',)


class PostEventAdmin(admin.ModelAdmin):
    list_display = ('text', 'post_image')


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id','Contact1', 'Address')


class FooterBusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city',  )


admin.site.register(Waste, WasteAdmin)
admin.site.register(CreatePickup, PickupAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(PostNews, PostNewsAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Goal, GoalAdmin),
admin.site.register(PostEvent, PostEventAdmin)
admin.site.register(FooterBusinessHours, FooterBusinessHoursAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Footer, FooterAdmin)