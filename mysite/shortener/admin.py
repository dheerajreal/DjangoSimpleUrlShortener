from django.contrib import admin
# Register your models here.
from .models import UrlRecord
# change admin interface
admin.site.index_title = "Simple URL Shortener admin"
admin.site.site_header = "Simple URL Shortener admin"
admin.site.site_title = "Simple URL Shortener admin"
admin.site.site_url = "/"


class UrlRecordAdmin(admin.ModelAdmin):
    # things to go on admin page
    list_display = ["original_url", "short_url"]
    # can filter by date_created
    list_filter = ["date_created"]
    # allow search
    search_fields = ["original_url", "short_url"]


admin.site.register(UrlRecord, UrlRecordAdmin)
