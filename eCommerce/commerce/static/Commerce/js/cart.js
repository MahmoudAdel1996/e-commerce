function delete_from_cart(entry){
    var $entry = $(entry);
    var id = $entry.data('id');
    $.ajax({
        url: '/delete_from_cart/'+ id +'/',
        method: 'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('x-CSRFToken', csrf_token)
        },
        success: function (data) {
            $('#lenCard').text(data);
            $entry.parent().parent().parent().parent().remove();
            $.notify("Product removed", "error");
            if (data === '0'){
                $('.container').load(' .container');
            }
        }
    })
}

function buy(){
    $.ajax({
        url: '/cart/buy/',
        method: 'POST',
        beforeSend: function(xhr){
            xhr.setRequestHeader('x-CSRFToken', csrf_token)
        },
        success: function (data) {
            if (data === "Successful"){
                $.notify(data, "success");
                $('.card').remove()
                $('#lenCard').text('0');
                $('.container').load(' .container');
            }
            else{
                $.notify("Error, No products on cart", "error");
            }
        }
    })
}