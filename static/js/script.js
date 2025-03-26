document.getElementById('predictForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const textInput = document.getElementById('textInput').value;

    // Check if the input text is empty
    if (textInput.trim() === "") {
        alert("Please enter a comment.");
        return;
    }

    // Send a POST request to the backend to predict toxicity
    fetch('https://cyber-security-gb3e.onrender.com/predict', {
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

function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('show');

    // Close menu when clicking outside
    document.addEventListener('click', function (event) {
        const isClickInsideMenu = navLinks.contains(event.target);
        const isClickOnMenuIcon = event.target.classList.contains('menu-icon');

        if (!isClickInsideMenu && !isClickOnMenuIcon && navLinks.classList.contains('show')) {
            navLinks.classList.remove('show');
        }
    });
}

function fbSubmit() {
    const feedbackInput = document.getElementById("feedbackInput").value.trim();
    const feedbackMessage = document.getElementById("feedbackMessage");

    if (feedbackInput === "") {
        feedbackMessage.textContent = "Please enter your feedback before submitting.";
        feedbackMessage.style.color = "red";
        feedbackMessage.style.visibility = "visible";
    } else {
        feedbackMessage.textContent = "Thank you for your feedback!";
        feedbackMessage.style.color = "green";
        feedbackMessage.style.visibility = "visible";

        // Clear the textarea after submission
        document.getElementById("feedbackInput").value = "";
    }
};
