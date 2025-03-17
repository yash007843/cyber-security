document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const textInput = document.getElementById('textInput').value;

    // Check if the input text is empty
    if (textInput.trim() === "") {
        alert("Please enter a comment.");
        return;
    }

    // Send a POST request to the backend to predict toxicity
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => {
        const result = data.prediction;
        document.getElementById('result').innerText = "Prediction: " + result;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error occurred. Please try again.");
    });
});
