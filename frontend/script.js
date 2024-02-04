function fetchFruits() {
    const apiUrl = 'http://127.0.0.1:5000/api/get_fruits?email=juh@gmail.com'; // Replace with email

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if ('fruits' in data) {
            console.log(data['fruits']);
        } else {
            console.error('No "fruits" property found in the data object.');
        }

        const fruits = data['fruits'];
        const parentContainer = document.getElementById('parentContainer');

        // Handle case when there are no products
        if (!fruits.length) {
            parentContainer.innerHTML = '<p>Aucun produit disponible.</p>';
        } else {
            parentContainer.innerHTML = '';
        }

        fruits.forEach(product => {
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

function fetchVegs() {
    const apiUrl = 'http://127.0.0.1:5000/api/get_vegetables?email=juh@gmail.com'; // Replace with email

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if ('vegetables' in data) {
            console.log(data['vegetables']);
        } else {
            console.error('No "vegetables" property found in the data object.');
        }

        const vegetables = data['vegetables'];
        const parentContainer = document.getElementById('parentContainer');

        // Handle case when there are no products
        if (!vegetables.length) {
            parentContainer.innerHTML = '<p>Aucun produit disponible.</p>';
        } else {
            parentContainer.innerHTML = '';
        }

        vegetables.forEach(product => {
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
