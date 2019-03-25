#encoding: utf-8
from django.shortcuts import render
from .forms import PubCourseForm,CourseTeacher
from apps.course.models import Course,CourseCategory,Teacher
from django.views.generic import View
from utils import restful
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_POST,require_GET
from django.db.models import F,Count

@method_decorator(permission_required(perm="course.change_course",login_url='/'),name='dispatch')
class PubCourse(View):
    def get(self,request):
        context = {
            'categories': CourseCategory.objects.all(),
            'teachers': Teacher.objects.all()
        }
        return render(request,'cms/pub_course.html',context=context)

    def post(self,request):
        form = PubCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get("cover_url")
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            teacher_id = form.cleaned_data.get('teacher_id')

            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)

            Course.objects.create(title=title, video_url=video_url, cover_url=cover_url, price=price, duration=duration,
                                  profile=profile, category=category, teacher=teacher)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())

@require_GET
def course_category(request):
    categories=CourseCategory.objects.annotate(count=Count('course'))
    context={
        'categories':categories
    }
    return render(request,'cms/course_category.html',context=context)
@require_POST
def add_course_category(request):
    name=request.POST.get('name')
    exists=CourseCategory.objects.filter(name=name).exists()
    if not exists:
        CourseCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已经存在！')

@require_POST
def edit_course_category(request):
    pk=request.POST.get('pk')
    name=request.POST.get('name')
    try:
        CourseCategory.objects.filter(pk=pk).update(name=name)
        return restful.ok()
    except:
        return restful.params_error(message='该分类不存在！')

@require_POST
def delete_course_category(request):
    pk=request.POST.get('pk')
    try:
        CourseCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该分类不存在！')

class AddCourse_Teacher(View):
    def get(self,request):
        return render(request,'cms/cource_teacher.html')

    def post(self,request):
        form=CourseTeacher(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            avatar=form.cleaned_data.get('avatar')
            jobtitle=form.cleaned_data.get('jobtitle')
            profile=form.cleaned_data.get('profile')
            Teacher.objects.create(username=username,avatar=avatar,jobtitle=jobtitle,profile=profile)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())
@require_GET
def course_teacher_list(request):
    teacher=Teacher.objects.annotate(count=Count('course'))
    context={
        'teachers':teacher
    }
    return render(request,'cms/teacher_list.html',context=context)
@require_POST
def delete_teacher(request):
    pk = request.POST.get('pk')
    print(pk)
    try:
        Teacher.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该讲师不存在！')