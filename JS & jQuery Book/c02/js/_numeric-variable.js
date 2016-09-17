// Create three variables to store the info needed
var price;
var quantity;
var total;

// Assign values to the price and quantity variables.
price = 5;
quantity = 14;
// Calculate total by multiplying price by quantity.
total = price * quantity;

//Get the element with an id of cost.
var el = document.getElementbyId('cost');
el.textContent = '$' + total;

/*
NOTE: textContent does not work in IE8 or earlier
You can use innter HTML, but note the security issues on p228-231
el.innerHTML = '$' + total;
*/
