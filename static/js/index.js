
function doDisplay(){
    const option = document.getElementById("coin_type");
    const unit_value = document.getElementById("unit_value")
    if(option.value=="minutes"){
        unit_value.disabled=false;
    }else{
        unit_value.disabled=true;
    }
}


window.onload = function(){
    const input  = document.querySelector('#coin_type');
    input.addEventListener('change', doDisplay);
}
