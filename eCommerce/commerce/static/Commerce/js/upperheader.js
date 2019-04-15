$(window).ready(function(){
    $('.search-bar2').hide();
    $('.search-btn').click(function () {
        if ($(window).width() < 635){
            $('.search-bar2').toggle()
        }
    })
});