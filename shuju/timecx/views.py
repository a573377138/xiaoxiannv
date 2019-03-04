from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.db import connection
from django.views.generic import View
import json
from io import StringIO,BytesIO
import openpyxl


# Create your views here.
def renwu(request):
    if request.method == 'GET':
        return render(request, 'renwu.html')
    elif request.method == 'POST':
        global kasj,jssj
        kasj = request.POST.get('kssj')
        jssj = request.POST.get('jssj')
        return render(request, 'renwuxq.html')
def renwuxq(request):
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

    dic = {
        'draw': draw,
        'recordsTotal': count,
        'recordsFiltered': count,
        'data': data,
    }
    return HttpResponse(json.dumps(dic), content_type='application/json')
def select_all():
    cursor = connection.cursor()
    sql = '''select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,biaoji,role_type,
    dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级 from renwu where record_date<date'{0}' and record_date>=date'{1}' order by dbname'''.format(jssj,kasj)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def select_by_page(start, end):
    cursor = connection.cursor()
    sql = """
        select * from
            (select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,biaoji,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级,rownum as rn
            from renwu where record_date<date'{0}' and record_date>=date'{1}' order by dbname )
        where rn>=%s and rn<%s
        """.format(jssj,kasj)
    cursor.execute(sql, [start, end])
    result = cursor.fetchall()
    cursor.close()
    return result

def all_count():
    cursor = connection.cursor()
    sql = "select count(*) from renwu where record_date<date'{0}' and record_date>=date'{1}'".format(jssj,kasj)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0]

def query(search_key):
    cursor = connection.cursor()
    sql = '''select c.*,d.alltime,d.biaoji,d.d_bname,d.dltag,d.role_type,d.tag,d.tbcost,d.time,d.tongbao,d.精练等级,d.装备分数,d.镶嵌等级,d.最大精练,d.最大镶嵌 from
    (select accountname,dbname,rolename,count(*)renwushu,roleid from 
    (select /*+parallel(r,2)+*/* from xsjods.jx3_role_log_opeartion r
    where actiontype=9
    and record_date>=to_date('{0}','yyyy-MM-dd HH24:mi:ss')
    and record_date<to_date('{1}','yyyy-MM-dd HH24:mi:ss')
    )a
    left join 
    jx3_real_ods.tmp_renwu_chongfu b
    on(to_number(a.col_3)=b.task_id)
    where b.task_id is null
    group by accountname,dbname,rolename,roleid) c
    inner join
    (select * from renwu where record_date>=date'{2}' and record_date<date'{3}') d
    on (c.accountname=d.accountname
    and c.dbname=d.dbname
    and c.roleid=d.roleid)'''.format(search_key[0], search_key[1], kasj, jssj)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = '''select count(*) from renwu where dbname like '%%{0}%%' and record_date<date'{1}' and record_date>=date'{2}' '''.format(search_key,jssj,kasj)
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    cursor.close()
    return result, count
def quanliang(request):
    cursor = connection.cursor()
    sql = '''select d_bname,accountname,dbname,rolename,renwushu,roleid,tag,tongbao,time,tbcost,biaoji,alltime,role_type,dltag,装备分数,最大精练,最大镶嵌,精练等级,镶嵌等级 
    from renwu where record_date<date'{0}' and record_date>=date'{1}'order by dbname'''.format(jssj,kasj)
    cursor.execute(sql)
    deta = cursor.fetchall()
    title =[i[0] for i in cursor.description]
    cursor.close()
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename={}任务数据.xlsx'.format(kasj)
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
