function errorHandler() {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = "Invalid Number";
}

function successHandler() {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = "Success";
}