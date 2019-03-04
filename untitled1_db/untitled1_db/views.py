from django.shortcuts import render
from django.db import connection

def index(request):
    cur = connection.cursor()
    cur.execute("insert into TEST1(id,name,PARENTID) values (3,'红楼梦','100')")
    return render(request,'index.html')
