window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (){ //$-getElementByClass
        let t_href = event.target;
        console.log(t_href.name); //basket_id
        console.log(t_href.value); //basket_quantity

        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function(data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });
}