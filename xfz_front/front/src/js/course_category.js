function NewsCategory() {

}

NewsCategory.prototype.run =function () {
    var self=this;
    self.listenAddCategory();
    self.listeneEditCategory();
    self.listenDeleteCategory();
};

NewsCategory.prototype.listenAddCategory =function(){
    var addBtn=$('#add-btn');
    addBtn.click(function () {
        xfzalert.alertOneInput({
            'title':'添加课程分类名',
            'text':'请不要输入过长的名字',
            'placeholder':'请输入课程分类',
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/add_course_category/',
                    'data':{
                        'name':inputValue
                    },
                    'success':function (result) {
                        if(result['code']===200){
                            console.log(result);
                            window.location.reload();
                        }else {
                            xfzalert.close();
                        }
                    }
                })
            }
        })
    })
};

NewsCategory.prototype.listeneEditCategory =function(){
    var self=this;
    var editBtn=$('.edit-btn');
    editBtn.click(function () {
        var dangqianBtn=$(this);
        var tr=dangqianBtn.parent().parent();
        var pk=tr.attr('data-pk');
        var name=tr.attr('data-name');
        xfzalert.alertOneInput({
            'title':'修改新闻分类名称',
            'placeholder':'请输入新的分类名称',
            'value':name,
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/edit_course_category/',
                    'data':{
                        'pk':pk,
                        'name':inputValue
                    },
                    'success':function (result) {
                        if(result['code']===200){
                            window.location.reload();
                        }else {
                            xfzalert.close();
                        }
                    }
                })

            }

        })
    })
};

NewsCategory.prototype.listenDeleteCategory=function(){
    var deleteBtn=$('.delete-btn');
    deleteBtn.click(function () {
        var dqscBtn=$(this);
        var tr=dqscBtn.parent().parent();
        var pk=tr.attr('data-pk');
        xfzalert.alertConfirm({
            'title':'确认删除该分类？',
            'confirmCallback':function () {
                xfzajax.post({
                    'url':'/cms/delete_course_category/',
                    'data':{
                        'pk':pk
                    },
                    'success':function (result) {
                        if(result['code']===200){
                            window.location.reload();
                        }else {
                            xfzalert.close();
                        }
                    }
                })
            }
            }
        )
    })
};


$(function () {
   var category= new NewsCategory();
    category.run();
});