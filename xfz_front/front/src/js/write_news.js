function News() {

}



News.prototype.listenUploadFileEvent=function(){
    var uploadBtn=$('#upload-btn');
    uploadBtn.change(function () {
       var file=uploadBtn[0].files[0];
       var formData=new FormData();
       formData.append('file',file);
       xfzajax.post({
           'url':'/cms/upload_file/',
           'data':formData,
           'processData':false,
           'contentType':false,
           'success':function (result) {
               if(result['code']===200){
                  var url=result['data']['url'];
                  var thumbnailInput=$('#thumbnail-form');
                  thumbnailInput.val(url);
               }
           }

       })
    });

};

News.prototype.listenQnUploadFileEvent=function(){
    var self=this;
    var uploadBtn=$('#upload-btn');
    uploadBtn.change(function () {
        xfzajax.get({
            'url':'/cms/qntoken/',
            'success':function (result) {
                if(result['code']===200){
                    var token=result['data']['token'];
                    var key = (new Date()).getTime() + '.' + file.name.split('.')[1];
                    var putExtra = {
                        fname: key,
                        params:{},
                        mimeType: ['image/png','image/jpeg','image/gif','video/x-ms-wmv']
                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: xiao_xiannv.region.z2
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

News.prototype.run= function(){
    var self=this;
    // self.listenUploadFileEvent();
    self.listenQnUploadFileEvent();
};


$(function () {
   var news=new News();
   news.run();
});