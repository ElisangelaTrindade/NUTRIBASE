window.addEventListener("load", function() {
    (function($) {
        $(document).ready(function() {
            $(".submit-row").prepend("Total de calorias: <div id='total' style='display: inline'>0</div><br /><br />");
            $('select[id*="id_meal-meal-content_type-object_id-"]').change(function() {
                $.calculateTotalOfCalories(django.jQuery)
            });
            $('input[id*="id_meal-meal-content_type-object_id-"]').focusout(function() { 
                $.calculateTotalOfCalories(django.jQuery)
            })
        });

    })(django.jQuery);
});


$.calculateTotalOfCalories = function($) {
    var total=0
    $('select[id*="id_meal-meal-content_type-object_id-"]').each(function(){
        var calories=$(this).find(":selected").attr('calories')
        var base_weight=$(this).find(":selected").attr('base_weight')
        if (calories && base_weight) {
            const re = /id_meal-meal-content_type-object_id-(\d+)-mealfood_set-(\d+)-food/gi
            var result=re.exec($(this).attr('id'))
            var group_expected_id=result[1]
            var weight_expected_id=result[2]
            var selector_weigth=$('input[id="id_meal-meal-content_type-object_id-' + group_expected_id.toString() + '-mealfood_set-' + weight_expected_id.toString() + '-weight"]')
            if (selector_weigth) {
                var weight=$(selector_weigth).val()
                if (weight) {
                    total+=weight*calories/base_weight
                }
            }
        }
    })
    $("#total").text(total.toFixed(2).toString())
}
