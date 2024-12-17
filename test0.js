// Get input elements by their IDs
let title = document.getElementById('title');
let price = document.getElementById('price');
let taxes = document.getElementById('taxes');
let ads = document.getElementById('ads');
let discount = document.getElementById('discount');
let total = document.getElementById('total');
let count = document.getElementById('count');
let category = document.getElementById('catgory');
let submit = document.getElementById('submit');

// Function to calculate the total price
function gettotal() {
    // Validate if the price field is not empty
    if (price.value !== '') {
        // Parse input values to ensure they are treated as numbers
        let priceValue = parseFloat(price.value) || 0;
        let taxesValue = parseFloat(taxes.value) || 0;
        let adsValue = parseFloat(ads.value) || 0;
        let discountValue = parseFloat(discount.value) || 0;

        // Calculate the total price
        let totalPrice = priceValue + taxesValue + adsValue - discountValue;

        // Display the result in the total element
        total.innerHTML = totalPrice.toFixed(2);

        // Set a success background
        total.style.background = '#040';
    } else {
        // Reset total and change background to red for invalid input
        total.innerHTML = '';
        total.style.background = '#f00';
    }

    console.log('Total calculation done');
}

