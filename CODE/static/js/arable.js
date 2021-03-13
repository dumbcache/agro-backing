$(document).ready(function(){
    $('#for_arable').hide();
    $('#Poly').hide();
    $('#Mono').hide();
})
$('#kind_of_arable').change(function(){
    $('#for_arable').show();
})
$('#taste_of_crop').change(function(){
    if($(this).val()=="none"){
        $('#Poly').hide();
        $('#Mono').hide();
    }
    else if($(this).val()=="Monoculture"){
        $('#Poly').hide();
        $('#Mono').show();
    }
    else if($(this).val()=="Polyculture"){
        $('#Mono').hide();
        $('#Poly').show();
    }
})