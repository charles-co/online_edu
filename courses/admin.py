from django.contrib import admin
from .models import Subject, Course, Module, Video, Text, Image, Content

# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

class ModuleInline(admin.StackedInline):
    model = Module

class ContentInline(admin.StackedInline):
    model = Content

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline]

class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline]

admin.site.register(Module, ModuleAdmin)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Text)
