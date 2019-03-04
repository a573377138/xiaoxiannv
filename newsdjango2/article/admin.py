from django.contrib import admin
from .models import Category,Item,Article,Tag,Ad

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','item_count')

    #统计分类下面有多少子栏目
    def item_count(self,obj):
        return Item.objects.filter(categorys=obj.id).count()

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','categorys','completed')



class ArticleAdmin(admin.ModelAdmin):
    #列表显示字段
    list_display = ('title', 'item', 'status', 'author', 'publish_date',
                    'expiration_date', 'is_active')

    list_filter = ('author', 'status', 'is_active', 'publish_date',
                   'expiration_date')
    #每页记录数
    list_per_page = 25
    #查询字段
    search_fields = ('title', 'tags', 'slug', 'content')

    class Media:
        js = ('/static/ueditor/ueditor.config.js', '/static/ueditor/ueditor.all.min.js',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')

    def article_count(self, obj):
        #return obj.article_set.count()
        return Article.objects.filter(tags=obj.id).count()


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic', 'adurl', 'adlocation','status')


admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Ad,AdAdmin)




admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)