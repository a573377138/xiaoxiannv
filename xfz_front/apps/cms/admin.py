from django.contrib import admin
from apps.course.models import Teacher,Course
# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['username','avatar','jobtitle','profile','course_count']
    fields = ['username','avatar','jobtitle','profile']
    search_fields = ['username']
    list_display_links=['username','jobtitle']
    # inlines = [CourseInline, ]
    def course_count(self,obj):
        return Course.objects.filter(teacher=obj.id).count()

# class CourseInline(admin.TabularInline):
#     model = Course
