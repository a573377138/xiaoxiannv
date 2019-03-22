function CourseDetail() {
}

CourseDetail.prototype.initPlayer = function () {
    var videoInfoSpan = $("#video-info");
    var video_url = videoInfoSpan.attr("data-video-url");
    var cover_url = videoInfoSpan.attr("data-cover-url");
    var course_id = videoInfoSpan.attr('data-course-id');

    var player = cyberplayer("playercontainer").setup({
            width: '100%',
            height: '100%',
            file: video_url,
            image: cover_url,
            autostart: false,//是否自动开始
            stretching: "uniform",
            repeat: false,//是否需要重复
            volume: 100,//默认音量
            controls: true,//是否显示底部控制栏
            //primary:'flash', 强制使用flash播放
            tokenEncrypt: true,//是否采用token加密
            // AccessKey
            ak: 'e40c5fcb0bc34a10bd56a09e2711f7f5'
        });

        player.on('beforePlay',function (e) {
            if(!/m3u8/.test(e.file)){
                return;
            }
            xfzajax.get({
                'url': '/course/course_token/',
                'data': {
                    'video': video_url,
                    'course_id': course_id
                },
                'success': function (result) {
                    if(result['code'] === 200){
                        var token = result['data']['token'];
                        player.setToken(e.file,token);
                    }else{
                        window.messageBox.showInfo(result['message']);
                        player.stop();
                    }
                },
                'fail': function (error) {
                    console.log(error);
                }
            });
        });
};

CourseDetail.prototype.run = function () {
    this.initPlayer();
};


$(function () {
    var courseDetail = new CourseDetail();
    courseDetail.run();
});
