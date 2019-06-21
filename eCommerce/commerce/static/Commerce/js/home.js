function add_to_cart(entry){
    let $entry = $(entry);
    let id = $entry.data('id');
    let quantity = $entry.parent().prev().children("input").val();
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

    //for slider
    $.ajax({
        url: '/recommender/',
        method: 'GET',
        success: function (data) {
            $('.spinner-border').remove();
            for (let i = 0; i < data.length; i++) {
                $('#recommend').append(card(data[i]));
            }
            $('.recommend-container').append(pagination);
            new Swiper('.recommend-container', {
              grabCursor: true,
              centeredSlides: true,
              slidesPerView: '5',
              loop: true,
              autoplay: {
                delay: 2500,
                disableOnInteraction: false
              },
              pagination: {
                el: '.swiper-pagination',
                clickable: true
              },
              navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev'
              }
            });
        }
    });

    // install swiper for slider
    new Swiper('.best-seller-container', {
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: '5',
      loop: true,
      autoplay: {
        delay: 2500,
        disableOnInteraction: false
      },
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


function card(product) {
    return `<div class="swiper-slide text-center">
    <a class="card-link" href="\\product\\${product.pk}">
        <img class="card-img-top" src="\\media\\${product.fields.image}" alt="${product.fields.name}">
        <div class="card-body">
          <div class="text-dark font-weight-bold text-center">${product.fields.name.substring(0, 25)}</div>
          <div class="text-center text-danger impact">\$ ${product.fields.price}</div>
        </div>
    </a>
</div>`;
}
function pagination() {
   return `<div class="swiper-pagination"></div>
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>`;
}