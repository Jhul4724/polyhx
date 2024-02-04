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