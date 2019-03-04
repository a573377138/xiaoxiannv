from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse,JsonResponse
import json
import openpyxl
from io import StringIO,BytesIO
import json
from decimal import Decimal

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
# Create your views here.
def index(request):
    return render(request, 'index.html')

# 進入後端分頁示例頁面
def paging(request):
    draw = int(request.POST.get('draw',0))  # 記錄操作次數
    start = int(request.POST.get('start',0))  # 起始位置
    length = int(request.POST.get('length',0))  # 每頁長度
    search_key = request.POST.get('search[value]',0)  # 搜索關鍵字
    order_column = request.POST.get('order[0][column]')  # 排序字段索引
    order_column = request.POST.get('order[0][dir]')  #排序規則：ase/desc
    if search_key:
        result, count = query(search_key)
        data = result[start:start + length]
    else:
        data = select_by_page(start, start + length)
        count = all_count()
    for i in data:
        i=str(i[9])
    dic = {
        'draw': draw,
        'recordsTotal': count,
        'recordsFiltered': count,
        'data': data,
    }

    return HttpResponse(json.dumps(dic), content_type='application/json',default=default)
def select_all():
    cursor = connection.cursor()
    # Object of type 'datetime' is not JSON serializable ,用to_char轉換
    # ORA-00911: invalid character ,去掉分號
    sql = '''select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,tbcost,biaoji,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级 from renwu where record_date<date'2019-01-03' and record_date>=date'2019-01-02' order by dbname'''
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

# sql做分頁
def select_by_page(start, end):
    cursor = connection.cursor()
    sql = """
        select * from
            (select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,tbcost,biaoji,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级,rownum as rn
            from renwu where record_date<date'2019-01-03' and record_date>=date'2019-01-02' order by dbname )
        where rn>=%s and rn<%s
        """
    cursor.execute(sql, [start, end])
    result = cursor.fetchall()
    cursor.close()
    return result

def all_count():
    cursor = connection.cursor()
    sql = "select count(*) from renwu where record_date<date'2019-01-03' and record_date>=date'2019-01-02'"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0]

def query(search_key):
    cursor = connection.cursor()
    sql = '''select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,tbcost,biaoji,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级 from renwu where dbname like '%%%s%%' and record_date<date'2019-01-03' and record_date>=date'2019-01-02' ''' % search_key
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = '''select count(*) from renwu where dbname like '%%%s%%' and record_date<date'2019-01-03' and record_date>=date'2019-01-02' ''' % search_key
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    cursor.close()
    return result, count
def quanliang(request):
    cursor = connection.cursor()
    sql = '''select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,tbcost,biaoji,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级 
    from renwu where record_date<date'2019-01-03' and record_date>=date'2019-01-02'order by dbname'''
    cursor.execute(sql)
    deta = cursor.fetchall()
    title =[i[0] for i in cursor.description]
    cursor.close()
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename={}数据信息.xlsx'
    wb=openpyxl.Workbook()
    ws=wb.active
    for col in range(len(title)):
        c=col + 1
        ws.cell(row=1,column=c).value=title[col]
    for row in range(len(deta)):
        ws.append(deta[row])
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
