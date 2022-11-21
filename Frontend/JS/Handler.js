function errorHandler(msg) {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = msg;
    errorMsg[0].style.color = "red";
}

function successHandler() {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = "Success";
    errorMsg[0].style.color = "green";
}