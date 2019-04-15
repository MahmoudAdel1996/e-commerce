function add_to_cart(entry){
    var $entry = $(entry);
    var id = $entry.data('id');
    $.ajax({
        url: '/add_to_cart/'+ id +'/',
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