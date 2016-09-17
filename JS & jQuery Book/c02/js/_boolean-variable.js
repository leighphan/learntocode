// Create variables and assign their values
var inStock;
var shipping;
inStock = true;
shipping = false;

// Get the element that has an id of stock
var elStock = document.getElementById('stock');
// Set class name with value of inStock variable
elStock.className = inStock;
// Script is referencing ids from .html file

// Get the element that has an id of shipping
var elShip = document.getElementById('shipping');
// Set class name with value of shipping variable
elShip.className = shipping;
/*If id is 'shipping' then stock is 'false' (not in stock)
If id is 'stock' then stock is 'true' (in stock)
*/
