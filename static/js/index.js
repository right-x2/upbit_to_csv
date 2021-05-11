
function doDisplay(){
    var option = document.getElementById("coin_type");
    var box = document.getElementById("unit")
    console.log(box)
    if(option.value=="minutes"){
        box.style.display="block";
    }else{
        box.style.display="none";
    }
    console.log(option.value)
}

window.onload = function(){
    const input  = document.querySelector('#coin_type');
    console.log(input)
    input.addEventListener('change', doDisplay);
}
