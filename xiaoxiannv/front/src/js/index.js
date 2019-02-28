function Banner() {
    this.bannerWidth =1106;
    this.bannerGroup=$('#banner-group');
    this.index =1;
    this.leftArrow =$('.left-arrow');
    this.rightArrow= $('.right-arrow');
    this.bannerUL=$('#banner-ul');
    this.liList = this.bannerUL.children('li');
    this.bannerCount = this.liList.length;
    this.pageControl= $('.page-control');

}

Banner.prototype.initPageControl =function(){
    var self =this;
    for(var  i=0; i<self.bannerCount;i++){
        var circle = $("<li></li>");
        self.pageControl.append(circle);
        if(i ===0){
            circle.addClass("active");
        }
    }
    self.pageControl.css({"width":self.bannerCount*32})

};

Banner.prototype.initBanner = function(){
    var self = this;

    var firstBanner = self.liList.eq(0).clone();
    var lastBanner =self.liList.eq(self.bannerCount-1).clone();
    self.bannerUL.append(firstBanner);
    self.bannerUL.prepend(lastBanner);
    self.bannerUL.css({"width":self.bannerWidth*(self.bannerCount+2),"left":-self.bannerWidth});

};

Banner.prototype.toggleArrow =function(isShow){
    var self =this;
    if(isShow){
        self.leftArrow.show();
        self.rightArrow.show();
    }else {
        self.leftArrow.hide();
        self.rightArrow.hide();
    }

};

Banner.prototype.listenBannerHover = function() {
    var self =this;
    this.bannerGroup.hover(function () {
        clearInterval(self.timer);
        self.toggleArrow(true);
    },function () {
        self.loop();
        self.toggleArrow(false);
    });
};



Banner.prototype.loop = function(){
    var self =this;
    // var bannerUL=$('#banner-ul');
    // var index =0;
    // bannerUL.css({'left':-1180});
    this.timer = setInterval(function () {
        if(self.index>=self.bannerCount+1){
            self.bannerUL.css({'left':-self.bannerWidth});
            self.index=2;
        }else {
            self.index+=1;
        }
        self.animate();
    },2500);
};

Banner.prototype.listenArrowClick =function(){
    var self =this;
    self.leftArrow.click(function () {
        if(self.index ===0){
            self.bannerUL.css({"left":-self.bannerCount*self.bannerWidth});
            self.index=self.bannerCount-1;
        }else {
            self.index--;
        }
        self.animate();
    });
        self.rightArrow.click(function () {
        if(self.index ===self.bannerCount +1){
            self.bannerUL.css({"left":-self.bannerWidth});
            self.index =2;
        }else {
            self.index++;
        }
        self.animate();
    });
};

Banner.prototype.animate =function(){
    var self =this;
    self.bannerUL.animate({'left':-1106*self.index},500);
    var index =self.index;
    if(index ===0){
        index=self.bannerCount-1;
    }else if(index===self.bannerCount+1){
        index=0;
    }else {
        index=self.index-1;
    }
    self.pageControl.children('li').eq(index).addClass("active").siblings().removeClass('active');
};

Banner.prototype.listenPageControl=function(){
    var self=this;
    self.pageControl.children("li").each(function (index,obj) {
        $(obj).click(function () {
            self.index=index+1;
            self.animate();
        });
    });
};




Banner.prototype.run =function () {
    console.log('runing....');
    this.initBanner();
    this.initPageControl();
    this.loop();
    this.listenBannerHover();
    this.listenArrowClick();
    this.listenPageControl();
};

$(function () {
    var banner=new Banner();
    banner.run();
});