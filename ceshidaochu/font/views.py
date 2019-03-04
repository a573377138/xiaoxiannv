from django.shortcuts import render,HttpResponse
from io import StringIO,BytesIO
import xlwt
# Create your views here.
def output(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=user.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet(u'人员表单')
    #1st line
    sheet.write(0,0, '姓名')
    sheet.write(0,1, '英文名')
    sheet.write(0,2, '职位')
    sheet.write(0,3, '公司电话')
    sheet.write(0,4, '手机')
    sheet.write(0,5, 'QQ')
    sheet.write(0,6, 'MSN')
    sheet.write(0,7, 'Email')
    sheet.write(0,8, '办公地点')
    sheet.write(0,9, '部门')
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
def index(request):
    return render(request,'index.html')