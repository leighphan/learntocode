// Create the array and assign it values
var colors = ['white', 'black', 'custom'];

// Update the third item in the array
colors[2] = 'beige';
// Within the array 'colors' you get third item and change it to 'beige'

// Get the element with an id of colors
var el = document.getElementById('colors');
// Replace element with third item from the array
// In order to replace an item in a var, use 'textContent'
el.textContent = colors[2];

/*
NOTE: textContent does not work in IE8 or earlier
You can use innerHTML on line 10, but note the security issues on p228-231
el.innerHTML = colors[2];
*/
