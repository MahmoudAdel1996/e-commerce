$(document).ready(function(){
    $('.menu-bars').click(function(){
        $('.menu-close').removeClass('none');
        $('.menu-bars').addClass('none');
        $('nav').addClass('show');
        $('ul').addClass('show');
    })
    $('.menu-close').click(function(){
        $('.menu-bars').removeClass('none');
        $('.menu-close').addClass('none');
        $('nav').removeClass('show');
    })
    $('header ul a').click(function(){
        $('header ul a').removeClass('active');
        $(this).addClass('active');
    })
})
