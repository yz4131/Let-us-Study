function deleteOldRes() {
    const alreadyHas = document.getElementsByClassName("return_item");
    const imax = alreadyHas.length;
    for (let i=0; i<imax; i++) {
        alreadyHas[0].remove();
    }
}