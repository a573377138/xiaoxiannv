from django.shortcuts import render
from django.http import HttpResponse
import csv
import openpyxl
# Create your views here.
def shuju(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=数据.xlsx'
    # with open('1221-122外挂.xlsx','r') as fb:
    #     data=fb.read()
    # print(data)
    wb=openpyxl.load_workbook(r'C:\Users\houxianzhi\Desktop\1221-122外挂.xlsx')

    return response