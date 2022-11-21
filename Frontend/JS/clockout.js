const button = document.getElementsByClassName('out_btn');

button[0].addEventListener('click', async _ => {   
    var uid = document.getElementById("uid").value;
    var pwd = document.getElementById("psw").value;

    const url = 'https://3a0ou9wbb8.execute-api.us-east-2.amazonaws.com/v1/leave?id='+
                uid+'&pwd='+pwd;
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
        console.log("error");
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
        else if (data==="User hasn't enter any library") {
            errorHandler("You Haven't Entered Any Libraries");
        }
        else if (data==="Cannot get information") {
            errorHandler("It Seems Like You Don't Have An Account");
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