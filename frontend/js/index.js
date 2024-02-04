function identifyImage() {
    // const imagePath = document.getElementById('fileUrl').innerHTML;
    // console.log(imagePath)
    // if (!imagePath) {
    //     alert('Please enter an image path.');
    //     return;
    // }
    console.log("Inferring")
    return JSON.stringify("images": [
        "https://plant-id.ams3.cdn.digitaloceanspaces.com/similar_images/3/ac6/f7773aa980334d80ac50db8af1cce8a79ae16.jpeg",
        "https://plant-id.ams3.cdn.digitaloceanspaces.com/similar_images/3/35b/8ba1f3aa44dcdbef85f4dd81087b7d80f852d.jpeg"
    ],
    "name": "Rosa × odorata",
    "probability": 0.40463114)
    // fetch('http://127.0.0.1:5000/api/identify', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify({image_path: "https://www.1800flowers.com/blog/wp-content/uploads/2017/03/single-red-rose.jpg"}),
    // })
    // .then(response => response.json())
    // .then(data => {
    //     console.log("Done")
    //     document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    //     document.getElementById('apiResponse').textContent = 'Error calling API: ' + error.message;
    // });
}