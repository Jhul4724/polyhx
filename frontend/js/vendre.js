function fetchListings() {
    const apiUrl = 'http://127.0.0.1:5000/api/get_user_sales?email=juh@gmail.com'; // Replace with email

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if ('sales' in data) {
            console.log(data['sales']);
        } else {
            console.error('No "sales" property found in the data object.');
        }

        const sales = data['sales'];
        const parentContainer = document.getElementById('parentContainer');

        // Handle case when there are no products
        if (!sales.length) {
            parentContainer.innerHTML = '<p>Aucun produit disponible.</p>';
        } else {
            parentContainer.innerHTML = '';
        }

        sales.forEach(product => {
            // Create a new productContainer for each product
            const productContainer = document.createElement('div');
            productContainer.className = 'product-container';

            // Fill the productContainer with product details
            productContainer.innerHTML = `
                <div class="product">
                    <div class="product-image">
                        <img src="${product['image']}" alt="Image of ${product['name']}">
                    </div>
                    <div class="product-info">
                        <div class="productname"><h2>${product['name']}</h2></div>
                        <div class="productdescription"><p>${product['description']}</p></div>
                        <div class="productprice"><p>${product['price']}$/kg</p></div>
                    </div>
                </div>
            `;

            // Append the new productContainer to the parent container
            parentContainer.appendChild(productContainer);
        });
    })
    .catch(error => {
        console.error('Error fetching product data:', error);
        document.getElementById('parentContainer').innerHTML = '<p>Erreur lors du chargement des produits.</p>';
    });
}

// Code for the popup and the "Créer une annonce"
// JavaScript to handle the modal and form submission
document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('myModal');
    var btn = document.getElementById('myBtn');
    var span = document.getElementsByClassName('close')[0];
    var overlay = document.getElementById('overlay');

    // Function to open the modal
    btn.onclick = function() {
        modal.style.display = "block";
        overlay.style.display = "block";
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = "none";
        overlay.style.display = "none";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = closeModal;

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal || event.target == overlay) {
            closeModal();
        }
    }

    // Handling the form submission
    document.getElementById('listingForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        var formData = {
            email: 'wuh@gmail.com',
            name: document.getElementById('itemName').value,
            description: document.getElementById('itemDescription').value,
            image: document.getElementById('itemImage').value,
            price: parseFloat(document.getElementById('itemPrice').value),
            is_fruit: document.getElementById('itemType').value.toLowerCase() === 'fruits' ? true : false, // Convert to boolean based on 'fruits' or 'légumes'
            quantity: parseInt(document.getElementById('quantity').value, 10),
            status: 0 // Assuming status is always 0 as per your JSON example
        };
        
        // Send formData to your server with an API call using Fetch
        fetch('http://127.0.0.1:5000/api/create_new_sale', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json()) // Parse JSON response from the server
        .then(data => {
            console.log('Success:', data);
            alert('Listing added successfully!');
            closeModal();
            document.getElementById('listingForm').reset(); // Clear the form
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error adding listing: ' + error.message);
        });
    });
});
