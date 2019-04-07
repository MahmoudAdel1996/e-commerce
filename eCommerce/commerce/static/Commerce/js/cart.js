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
            if (data == 'login'){
                alert("You Should Login First.");
            }
            else{
                $('#lenCard').text(data);
                $entry.parent().parent().parent().parent().remove()
            }

        }
    })
}