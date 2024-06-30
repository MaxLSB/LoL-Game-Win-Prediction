document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const resultText = document.getElementById('resultText');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch('/predict_game', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const result = data.result[0];
            const probability = data.result[1];
            resultText.textContent = `Predicted Winner: ${result} (${(probability * 100).toFixed(2)}%)`;
        })
        .catch(error => {
            console.error('Error predicting game:', error);
            resultText.textContent = 'Prediction failed. Please try again.';
        });
    });
});
