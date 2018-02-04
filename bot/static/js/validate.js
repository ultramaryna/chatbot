var input = document.getElementById("id_name");
var button = document.getElementById("btn-start");
input.onkeyup = function(e) {
    if (input.value.length > 0) {
        button.classList.add("active");
    } else {
        button.classList.remove("active");
    }
};