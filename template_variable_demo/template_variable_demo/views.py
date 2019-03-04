from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username
def index(request):
    # p = Person('zhiliao')
    # context ={
    #     'Person':p
    # }
    # context = {
    #     'person':{
    #         'username':'张三'
    #     }
    # }
    context = {
        'persons': [
            '张三','李四','鲁班一号'
        ]
    }
    return render(request,'index.html',context=context)