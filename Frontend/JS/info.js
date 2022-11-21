const button = document.getElementsByClassName('info_btn');

button[0].addEventListener('click', async _ => {   
    var lib = document.getElementById("lib");
    var libname = lib.value;

    const url = 'https://3a0ou9wbb8.execute-api.us-east-2.amazonaws.com/v1/count?name='+libname;
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

        deleteOldRes();

        for (let i=0; i<data.length; i++){
            let obj = data[i];
            buildRes(obj);
        }
        successHandler();
    })
    .catch((error) => {
        console.error("FETCH ERROR:", error)
        errorHandler("Server Error");
    });   

});