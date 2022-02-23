$(document).ready(function (){

    $('.addtocartbtn').click(function (e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_quy = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_quy':product_quy,
                csrfmiddlewaretoken: token,
            },
            success: function(response){
                alertify
            }
        })
    } );
} );