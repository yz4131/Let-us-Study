function errorHandler() {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = "Invalid Number";
    errorMsg[0].style.color = "red";
}

function successHandler() {
    const errorMsg = document.getElementsByClassName("errorMsg");
    errorMsg[0].innerHTML = "Success";
    errorMsg[0].style.color = "green";
}