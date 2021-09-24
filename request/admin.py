from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Request


# Register your models here.
class RequestList(admin.ModelAdmin):
    list_display = ('username', 'request_date', 'status')
    list_filter = ('username', 'request_date')
    ordering = ['username']

admin.site.register(Request, RequestList)