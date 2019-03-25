function Teacher() {

}

Teacher.prototype.initUEditor =function(){
    window.ue=UE.getEditor('editor',{
        'initialFrameHeight': 100,
        'serverUrl': '/ueditor/upload/'
    });
};

Teacher.prototype.lisentQnloadfileEnvent=function(){
    var self=this;
    var loadfileBtn=$('#avatar-btn');
    loadfileBtn.change(function () {
        var file=this.files[0];
        xfzajax.get({
            'url':'/cms/qntoken/',
            'success':function (result) {
                if(result['code']===200){
                    var token = result['data']['token'];
                    // a.b.jpg = ['a','b','jpg']
                    // 198888888 + . + jpg = 1988888.jpg
                    var key = (new Date()).getTime() + '.' + file.name.split('.')[-1];
                    var putExtra = {
                        fname: key,
                        params:{},
                        mimeType: ['image/png','image/jpeg','image/gif','video/x-ms-wmv']
                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: qiniu.region.z2
                    };
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    observable.subscribe({
                        'next': self.handleFileUploadProgress,
                        'error': self.handleFileUploadError,
                        'complete': self.handleFileUploadComplete
                    });
                }

            }
        })
    })
};

Teacher.prototype.handleFileUploadProgress = function (response) {
    var total = response.total;
    var percent = total.percent;
    var percentText = percent.toFixed(0)+'%';
    // 24.0909，89.000....
    var progressGroup = Teacher.progressGroup;
    progressGroup.show();
    var progressBar = $(".progress-bar");
    progressBar.css({"width":percentText});
    progressBar.text(percentText);

};

Teacher.prototype.handleFileUploadError = function (error) {
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    console.log(error.message);
};

Teacher.prototype.handleFileUploadComplete = function (response) {
    console.log(response);
    var progressGroup = $("#progress-group");
    progressGroup.hide();

    var domain = 'http://poaqr3qgt.bkt.clouddn.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='teacher-avatar']");
    thumbnailInput.val(url);
};


Teacher.prototype.lisentSubmit=function(){
    var submitBtn=$('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();
        var name=$("input[name='teacher-username']") .val();
        var avatar=$("input[name='teacher-avatar']") .val();
        var job=$("input[name='jobtitle']") .val();
        var content=window.ue.getContent();

        xfzajax.post({
            'url':'/cms/addcourse_teacher/',
            'data':{
                'username':name,
                'avatar':avatar,
                'jobtitle':job,
                'profile':content
            },
            'success':function (result) {
                if(result['code']===200){
                    xfzalert.alertSuccess('添加讲师成功！',function () {
                        window.location=window.location.href;
                    })
                }
            }
        })
        }

    )
};


Teacher.prototype.run=function () {
  var self=this;
  self.initUEditor();
  self.lisentQnloadfileEnvent();
  self.lisentSubmit();
};

$(function () {
    var teacher=new Teacher();
    teacher.run();
    Teacher.progressGroup = $('#progress-group');
});