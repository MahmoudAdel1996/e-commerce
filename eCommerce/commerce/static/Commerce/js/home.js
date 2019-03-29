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
            if (data == 'login'){
                alert("You Should Login First.");
            }
            else{
                $('#lenCard').text(data);
            }

        }
    })
}

$( document ).ready(function(){
    $("nav ul li:first-child a").addClass('active');

});
