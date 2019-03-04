from django.shortcuts import render
from .models import Category,Tag,Item,Ad,Article
import os
from django.conf import settings
import codecs
from django.template.loader import render_to_string
from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger

# Create your views here.
HTML_DIR = os.path.join(settings.BASE_DIR,'templates/html')
def globl_init(request):
    # 取分类
    category_list = Category.objects.all()
    #广告
    ad_list = Ad.objects.all()
    #热门新闻
    hot_articles = Article.objects.filter(is_active=True)[0:5]

    return locals()

def index(request):

    #取分类
    category_list =  Category.objects.all()

    ad_list = Ad.objects.all()

    article_list = Article.objects.all()[0:20]

    hot_articles = Article.objects.filter(is_active=True)[0:5]

    return render(request,'index.html',locals())

def category(request):
    categoryid = request.GET.get('cid')

    item_list = Item.objects.filter(categorys=categoryid)
    article_list = Article.objects.filter(item__categorys=categoryid)
    article_list =get_page(request,article_list)
    curr_url = request.get_full_path()
    nPos = curr_url.find('&page')
    if nPos > 0:
        curr_url = request.get_full_path()[0:nPos]
    else:
        curr_url = request.get_full_path()
    return render(request, 'category.html', locals())


def article(request):

    id = request.GET.get('id')
    articlehtml='article_{}.html'.format(id)
    article_html = os.path.join(HTML_DIR,articlehtml)
    if not os.path.exists(article_html):
       article = Article.objects.get(id=id)

       category_list = Category.objects.all()
       # 广告
       ad_list = Ad.objects.all()
       # 热门新闻
       hot_articles = Article.objects.filter(is_active=True)[0:5]
       content = render_to_string('article.html', locals())
       with  codecs.open(article_html,'w',encoding='utf-8') as static_file:
           static_file.write(content)


    return  render(request,article_html,locals())

def search(request):
    # 取分类
    # category_list = Category.objects.all()
    #
    # ad_list = Ad.objects.all()
    #
    # hot_articles = Article.objects.filter(is_active=True)[0:5]
    strquery = request.GET.get('query')
    article_list = Article.objects.filter(title__contains=strquery)

    return render(request, 'index.html', locals())

    pass
def item(request):
    categoryid = request.GET.get('cid')
    itemid = request.GET.get('itemid')
    item_list = Item.objects.filter(categorys=categoryid)
    article_list = Article.objects.filter(item=itemid)
    article_list = get_page(request, article_list)
    curr_url = request.get_full_path()
    nPos = curr_url.find('&page')
    if nPos > 0:
        curr_url = request.get_full_path()[0:nPos]
    else:
        curr_url = request.get_full_path()
    return render(request, 'category.html', locals())


def tag(request):
    tagid=request.GET.get('tagid')

    article_list = Article.objects.filter(tags=tagid)
    article_list = get_page(request, article_list)
    curr_url = request.get_full_path()
    nPos = curr_url.find('&page')
    if nPos > 0:
        curr_url = request.get_full_path()[0:nPos]
    else:
        curr_url = request.get_full_path()
    return render(request, 'tag.html', locals())


def get_page(request,object_list):

    '''
       Paginator是如何工作的：
       我们使用希望在每页中显示的对象的数量来实例化Paginator类。
       我们获取到page GET参数来指明页数
       我们通过调用Paginator的 page()方法在期望的页面中获得了对象。
       如果page参数不是一个整数，我们就返回第一页的结果。如果这个参数数字超出了最大的页数，我们就展示最后一页的结果。
       我们传递页数并且获取对象给这个模板（template）。
       :param request:
       :param object_list:
       :return: object_list
       '''
    pagesize = 3
    paginator = Paginator(object_list, pagesize)
    try:
        page = int(request.GET.get('page', 1))
        object_list = paginator.page(page)
        # print article_list
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        object_list = paginator.page(1)
    return object_list