from django.contrib import admin
from .models import Team, ServiceItem, ServiceItemMessage
# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_order')

@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('team', 'service_item_name')

@admin.register(ServiceItemMessage)
class ServiceItemMessageAdmin(admin.ModelAdmin):
    list_display = ('service_item', 'comment_user')
