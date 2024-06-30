function onClickedPredictGame() {
    console.log("Predict Game button clicked");
    var blueFirstBlood = document.getElementById("blueFirstBlood").value;
    var blueKills = document.getElementById("blueKills").value;
    var blueDeaths = document.getElementById("blueDeaths").value;
    var blueAssists = document.getElementById("blueAssists").value;
    var blueDragons = document.getElementById("blueDragons").value;
    var blueTowersDestroyed = document.getElementById("blueTowersDestroyed").value;
    var blueGoldDiff = document.getElementById("blueGoldDiff").value;
    var blueExperienceDiff = document.getElementById("blueExperienceDiff").value;
    var redAssists = document.getElementById("redAssists").value;
    var redDragons = document.getElementById("redDragons").value;
    var redTowersDestroyed = document.getElementById("redTowersDestroyed").value;


    $.post("http://127.0.0.1:5000/predict_game", {
        blueFirstBlood: blueFirstBlood,
        blueKills: blueKills,
        blueDeaths: blueDeaths,
        blueAssists: blueAssists,
        blueDragons: blueDragons,
        blueTowersDestroyed: blueTowersDestroyed,
        blueGoldDiff: blueGoldDiff,
        blueExperienceDiff: blueExperienceDiff,
        redAssists: redAssists,
        redDragons: redDragons,
        redTowersDestroyed: redTowersDestroyed
    }, function(data, status) {
        console.log(data.result);
        var prediction = data.result[0];
        var probability = (data.result[1] * 100).toFixed(2);
        var resultText = "Prediction: " + (prediction === 1 ? "Blue Team Wins" : "Red Team Wins") + " with probability " + probability + "%";
        $("#uiPredictionResult h2").html(resultText);
    });
}
