function buildRes(obj) {
    var cap = obj.capacity;
    var libname = short2full(obj.name);
    var emp = obj.empty;

    var res_container = document.getElementById("grid-container3");
    var newItem = document.createElement('div');
    newItem.className = "return_item";

    var padd0 = document.createElement('p');
    newItem.appendChild(padd0);

    var title1 = document.createElement('div');
    title1.className = "return_title";
    title1.innerHTML = "Library Name: " + libname;
    newItem.appendChild(title1);

    var padd1 = document.createElement('p');
    newItem.appendChild(padd1);

    var title2 = document.createElement('div');
    title2.className = "return_title";
    title2.innerHTML = "Capacity: " + cap;
    newItem.appendChild(title2);

    var padd2 = document.createElement('p');
    newItem.appendChild(padd2);

    var title3 = document.createElement('div');
    title3.className = "return_title";
    title3.innerHTML = "Empty Seats: " + emp;
    newItem.appendChild(title3);

    res_container.appendChild(newItem);
}