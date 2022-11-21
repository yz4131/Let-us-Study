const button = document.getElementsByClassName('in_btn');

button[0].addEventListener('click', async _ => {   
    var uid = document.getElementById("uid").value;
    var pwd = document.getElementById("psw").value;
    var lib = document.getElementById("lib").value;

    const url = 'https://3a0ou9wbb8.execute-api.us-east-2.amazonaws.com/v1/enter?id='+
                uid+'&pwd='+pwd+'&name='+lib;
    fetch(url, {
        mode: 'cors',
        method: "GET",
        withCredentials: true,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then((response) => {
    if (response.ok) {
        console.log(response);
        return response.json();
    } else {
        console.log(response);
        console.log("error")
        errorHandler("Server Error");
        }
    })
    .then((data) => {
        console.log(data);
        if (data==="success") {
            successHandler();
        }
        else if (data==="wrong password") {
            errorHandler("Wrong Password");
        }
        else if (data==="already entered, please log off first") {
            errorHandler("You Have Already Entered A Library, Clock Out First");
        }
        else {
            errorHandler("Server Error");
        }
    })
    .catch((error) => {
        console.error("FETCH ERROR:", error)
        errorHandler("Server Error");
    });   
});