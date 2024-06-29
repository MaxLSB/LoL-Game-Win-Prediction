from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_game',methods=['POST'])
def predict_game():
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
    
    response = jsonify({
        'result': util.get_game_prediction(blueFirstBlood, blueKills, blueDeaths, blueAssists, blueDragons, blueTowersDestroyed, blueGoldDiff, blueExperienceDiff, redAssists, redDragons, redTowersDestroyed)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response
    

if __name__ == "__main__":
    print('Starting League of Legends Game Prediction Server...')
    util.load_saved_artifacts() 
    app.run()