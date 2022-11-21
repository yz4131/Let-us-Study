const button = document.getElementsByClassName('register_btn');

button[0].addEventListener('click', async _ => {   
    var psw1 = document.getElementById("psw1").value;
    var psw2 = document.getElementById("psw2").value;
    if (psw1 !== psw2) {
        errorHandler("Passwords Do Not Match");
    }
    else {
        var uid = document.getElementById("uid").value;

        const url = "https://3a0ou9wbb8.execute-api.us-east-2.amazonaws.com/v1/user";
        var data = {"id": uid, "pwd": psw1};
        fetch(url, {
            mode: 'cors',
            method: "POST",
            withCredentials: true,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
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
            if (data === "success") {
                successHandler();
            }
            else if (data==="Already exist") {
                errorHandler("User ID Already Exists");
            }
            else {
                errorHandler("Server Error");
            }
        })
        .catch((error) => {
            console.error("FETCH ERROR:", error);
            errorHandler("Server Error");
        });   
    }

});