from flask import Flask, request, jsonify, send_from_directory
import util

app = Flask(__name__, static_folder='../client')  # Adjusted static folder path

# Endpoint to serve your HTML file (not needed for /predict_game)
@app.route('/')
def index():
    return "This endpoint is not used."

# Endpoint to handle prediction request
@app.route('/predict_game', methods=['POST'])
def predict_game():
    # Extract data from the POST request form
    blueFirstBlood = int(request.form['blueFirstBlood'])
    blueKills = int(request.form['blueKills'])
    blueDeaths = int(request.form['blueDeaths'])
    blueAssists = int(request.form['blueAssists'])
    blueDragons = int(request.form['blueDragons'])
    blueTowersDestroyed = int(request.form['blueTowersDestroyed'])
    blueGoldDiff = int(request.form['blueGoldDiff'])
    blueExperienceDiff = int(request.form['blueExperienceDiff'])
    redAssists = int(request.form['redAssists'])
    redDragons = int(request.form['redDragons'])
    redTowersDestroyed = int(request.form['redTowersDestroyed'])

    # Call the function to get prediction
    result, probability = util.get_game_prediction(
        blueFirstBlood, blueKills, blueDeaths, blueAssists, blueDragons, blueTowersDestroyed,
        blueGoldDiff, blueExperienceDiff, redAssists, redDragons, redTowersDestroyed
    )

    # Return the prediction as JSON response
    return jsonify({
        'result': [result, probability]
    })

if __name__ == "__main__":
    print('Starting League of Legends Game Prediction Server...')
    util.load_saved_artifacts()  # Ensure artifacts are loaded correctly
    app.run()
