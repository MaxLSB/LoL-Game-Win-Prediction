function updateValue(id) {
    const slider = document.getElementById(id);
    const valueSpan = document.getElementById(id + 'Value');
    valueSpan.innerText = slider.value;
}

document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = result.prediction;
        document.getElementById('probabilities').innerHTML = `
            <p>Winning Team Probability: ${(result.winning_team_probability * 100).toFixed(2)}%</p>
        `;
    })
});
