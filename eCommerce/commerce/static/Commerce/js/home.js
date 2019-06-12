function add_to_cart(entry){
    var $entry = $(entry);
    var id = $entry.data('id');
    var quantity = $entry.parent().prev().children("input").val()
    $.ajax({
        url: '/add_to_cart/'+ id +'/' + quantity + "/",
        method: 'POST',
        beforeSend: function(xhr){
            xhr.setRequestHeader('x-CSRFToken', csrf_token)
        },
        success: function (data) {
            if (data === 'login'){
                $.notify("You Should Login First.", "info");
            }
            else{
                $('#lenCard').text(data);
                $.notify("This product added to cart successfully", "success");
            }

        }
    })
}

$( document ).ready(function(){
    $("nav ul li:first-child a").addClass('active');
    // install swiper
    var swiper = new Swiper('.swiper-container', {
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      loop: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
      }
    });
});
