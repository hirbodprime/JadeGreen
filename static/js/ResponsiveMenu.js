$(document).ready(function () {
    $('#humberger-menu').click(function(){
        var nav = $('.responsive-nav');
        nav.show();
        nav.animate({
            right : '0'
        },400);
        $('body').append('<div class="temp"></div>');
        $(".temp").click(function(){
            nav.animate({
                right : '-284px'
            },400,function(){
                nav.hide();
            });
            $(this).remove()
        })
    })
})