from django.contrib import admin
from .models import Result, DownloadableResource, News

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_code', 'course_title', 'grade', 'semester', 'academic_year')
    list_filter = ('semester', 'academic_year', 'grade')
    search_fields = ('student__username', 'course_code', 'course_title')


@admin.register(DownloadableResource)
class DownloadableResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pdf_file', 'icon_class')
    search_fields = ('title', 'description', 'icon_class')
    list_filter = ('title', 'description', 'icon_class')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'image', 'date')
    search_fields = ('title', 'excerpt')
    list_filter = ('date', 'title', 'excerpt')
    readonly_fields = ('date',)
