function FrontBase() {

}

FrontBase.prototype.run= function(){
    var self =this;
    self.listenAuehBoxHover();
    self.handleNavStatus();
};
FrontBase.prototype.listenAuehBoxHover=function(){
    var authbox = $('.auth-box');
    var usermorebox= $('.user-more-box');
    authbox.hover(function () {
        usermorebox.show();
    },function () {
      usermorebox.hide();
    });
};

FrontBase.prototype.handleNavStatus = function () {
    // http://127.0.0.1:8000/payinfo/
    var url = window.location.href;
    var protocol = window.location.protocol;
    var host = window.location.host;
    // http: + // + 127.0.0.1:8000
    var domain = protocol + '//' + host;
    var path = url.replace(domain,'');
    var navLis = $(".nav li");
    navLis.each(function (index,element) {
        // js => $(js对象)
        var li = $(element);
        var aTag = li.children("a");
        var href = aTag.attr("href");
        if(href === path){
            li.addClass("active");
            return false;
        }
    });
};


function Auth() {
    var self = this;
    self.maskWrapper = $('.mask-wrapper');
    self.scrollWrapper=$('.scroll-wrapper');
    self.smscaptcha= $('.sms-captcha-btn');
}
Auth.prototype.run = function () {
    var self =this;
    self.listenShowHideEvent();
    self.listenswitchEvent();
    self.listenSigninEvent();
    self.listenImgCaptchaEvent();
    self.listenSmsCaptcha();
    self.listenSignupEvent();
};

Auth.prototype.showEvent = function(){
    var self = this;
    self.maskWrapper.show();
};

Auth.prototype.hideEvent = function(){
    var self = this;
    self.maskWrapper.hide();
};

Auth.prototype.listenShowHideEvent = function(){
    var self =this;
    var signinBtn =$('.signin-btn');
    var signupBtn =$('.signup-btn');
    var closeBtn =$('.close-btn');
    var uwserV=$('.form-control');

    signinBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({'left':0});
    });
    signupBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({'left':-400});
    });
    closeBtn.click(function () {
       self.hideEvent();
       uwserV.reset();
       // uwserV.set(null);
       //  document.getElementById("password").reset()
    });
};

Auth.prototype.listenswitchEvent = function(){
    var self=this;
    var switcher=$('.switch');
    switcher.click(function () {
        var currentLeft = self.scrollWrapper.css("left");
        currentLeft=parseInt(currentLeft);
        if (currentLeft<0){
          self.scrollWrapper.animate({"left":0});
        }else {
            self.scrollWrapper.animate({"left":"-400px"});
        }
    });
};

Auth.prototype.listenImgCaptchaEvent=function(){
    var imgcaptcha =$('.img-captcha');
    imgcaptcha.click(function () {
        imgcaptcha.attr("src","/account/img_captcha/"+"?random="+Math.random())
        // imgcaptcha.attr("src","/account/img_captcha/"+"?random="+Math.random())
    })
};


Auth.prototype.listenSmsCaptcha=function(){
    var self =this;
    var telephoneInput=$(".signup-group input[name='telephone']");
    self.smscaptcha.click(function () {
       var telephone=telephoneInput.val();
        if(!telephone){
            messageBox.showError('请输入手机号码！');
        }
        xfzajax.get({
            'url':'/account/sms_captcha/',
            'data':{
                'telephone':telephone
            },
            'success':function (result) {
                if(result['code']===200){
                    self.smsSuccessEvent();
                }
            },
            'fail':function (error) {
                console.log(error);
            }
        })
    })
};

Auth.prototype.smsSuccessEvent=function(){
    var self=this;
    messageBox.showSuccess('短信验证码发送成功！');
    self.smscaptcha.addClass('disabled');
    var count= 20;
    self.smscaptcha.unbind('click');
    var timer=setInterval(function () {
        self.smscaptcha.text(count+'s');
        count-=1;
        if(count<=0){
            clearInterval(timer);
            self.smscaptcha.removeClass('disabled');
            self.smscaptcha.text('发送验证码');
            self.listenSmsCaptcha();
        }

        },1000);

};

Auth.prototype.listenSigninEvent= function(){
    var self = this;
    // var closeBtn =$('.close-btn');
    var signinGroup = $('.signin-group');
    var telephoneInput = signinGroup.find("input[name='telephone']");
    var passwordInput= signinGroup.find("input[name='password']");
    var rememberInput = signinGroup.find("input[name='remember']");
    var submitBtn=signinGroup.find(".submit-btn");

    submitBtn.click(function () {
        var telephone=telephoneInput.val();
        var password = passwordInput.val();
        var remember= rememberInput.prop("checked");

        xfzajax.post({
            'url':'/account/login/',
            'data':{
                'telephone':telephone,
                'password':password,
                'remember':remember?1:0
            },
            'success':function (result) {
                    self.hideEvent();
                    window.location.reload();
            },
            'fail':function (error) {
                console.log(error);

            }

        })
    })
};

Auth.prototype.listenSignupEvent = function () {
    var signupGroup = $('.signup-group');
    var submitBtn = signupGroup.find('.submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();
        var telephoneInput = signupGroup.find("input[name='telephone']");
        var usernameInput = signupGroup.find("input[name='username']");
        var imgCaptchaInput = signupGroup.find("input[name='img_captcha']");
        var password1Input = signupGroup.find("input[name='password1']");
        var password2Input = signupGroup.find("input[name='password2']");
        var smsCaptchaInput = signupGroup.find("input[name='sms_captcha']");

        var telephone = telephoneInput.val();
        var username = usernameInput.val();
        var img_captcha = imgCaptchaInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        var sms_captcha = smsCaptchaInput.val();

        xfzajax.post({
            'url': '/account/register/',
            'data': {
                'telephone': telephone,
                'username': username,
                'img_captcha': img_captcha,
                'password1': password1,
                'password2': password2,
                'sms_captcha': sms_captcha
            },
            'success': function (result) {
                window.location.reload();
            },
            'fail':function (error) {
                console.log(error);
                window.messageBox.showError('服务器内部错误！')

            }
        });
    });
};



$(function () {
    var auth = new Auth();
    auth.run()
});

$(function () {
   var frontbase = new FrontBase();
   frontbase.run();
});

$(function () {
    if(window.template){
        template.defaults.imports.timeSince = function (dateValue) {
            var date = new Date(dateValue);
            var datets = date.getTime(); // 得到的是毫秒的
            var nowts = (new Date()).getTime(); //得到的是当前时间的时间戳
            var timestamp = (nowts - datets)/1000; // 除以1000，得到的是秒
            if(timestamp < 60) {
                return '刚刚';
            }
            else if(timestamp >= 60 && timestamp < 60*60) {
                minutes = parseInt(timestamp / 60);
                return minutes+'分钟前';
            }
            else if(timestamp >= 60*60 && timestamp < 60*60*24) {
                hours = parseInt(timestamp / 60 / 60);
                return hours+'小时前';
            }
            else if(timestamp >= 60*60*24 && timestamp < 60*60*24*30) {
                days = parseInt(timestamp / 60 / 60 / 24);
                return days + '天前';
            }else{
                var year = date.getFullYear();
                var month = date.getMonth();
                var day = date.getDay();
                var hour = date.getHours();
                var minute = date.getMinutes();
                return year+'/'+month+'/'+day+" "+hour+":"+minute;
            }
        }
    }
});