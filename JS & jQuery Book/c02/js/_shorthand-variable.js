/* METHOD 1
Variables declared and values assigned in same statement.
*/

var price = 5;
var quantity = 14;
var total = price & quantity;

/* METHOD 2
Three variables declared then values assigned to each
*/
var price, quantity, total;
price = 5;
quantity = 14;
total = price * quantity;

/* METHOD 3
Two vars declared and assigned on same line. Then one var declared and assigned on next line. */
var price = 5, quantity = 14;
var total = price * quantity;

// Write the total into element with id of cost
var el = document.getElementById('cost'); // Gets element w/ an id of cost
el.textContent = '$' + total; // Replaces content of this element.

/*Here a var is used to hold a ref to an element in the HTML page. This allows you to work directly w/ the element stored in that variable.*/

/*
NOTE: textContent does not work in IE8 or earlier
You can use innerHTML on line 20, but note the security issues on p228-231
el.innerHTML = '$' + total;
*/
