/**
 * Created by aibuz on 2017/10/12.
 */
$(document).ready(function() {
    $("#tijiao").click(function(){
        $('div.loading').show();
        $.ajax({
            url: "denglu/",
            type: 'GET',
            data: {},
            success: function (response) {
                var content = response.content;
                $('#dis').html(content);
                $('div.loading').hide();
            },
            error: function () {
                $('#content').html('server error...');

                //请求完成，隐藏模态框
                $('div.loading').hide();
            }
        })
    })
});