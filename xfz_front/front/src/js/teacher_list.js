function TeacherList() {

}


TeacherList.prototype.lisentDeleteBtn=function(){
        var deleteBtn=$('.delete-btn');
        deleteBtn.click(function () {
            var schuBtn=$(this);
            var tr=schuBtn.parent().parent();
            var pk=tr.attr('data-pk');
            xfzalert.alertConfirm({
                'title':'确定删除该讲师吗？',
                'confirmCallback':function () {
                    xfzajax.post({
                        'url':'/cms/delete_teacher/',
                        'data':{
                            'pk':pk
                        },
                        'success':function (result) {
                            if(result['code']===200){
                                window.location=window.location.href;
                            }
                            else {
                                xfzalert.close();
                            }
                        }
                    })
                }
            })
    })
};


TeacherList.prototype.run=function () {
    var self=this;
    self.lisentDeleteBtn();
};

$(function () {
    var teacherlist=new TeacherList();
    teacherlist.run();
});