from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('lol_model.pickle', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    features = {
        'blueFirstBlood': [int(data['blueFirstBlood'])],
        'blueKills': [int(data['blueKills'])],
        'blueDeaths': [int(data['blueDeaths'])],
        'blueAssists': [int(data['blueAssists'])],
        'blueDragons': [int(data['blueDragons'])],
        'blueTowersDestroyed': [int(data['blueTowersDestroyed'])],
        'blueGoldDiff': [int(data['blueGoldDiff'])],
        'blueExperienceDiff': [int(data['blueExperienceDiff'])],
        'redAssists': [int(data['redAssists'])],
        'redDragons': [int(data['redDragons'])],
        'redTowersDestroyed': [int(data['redTowersDestroyed'])]
    }
    
    features_df = pd.DataFrame(features)
    
    prediction = model.predict(features_df)[0]
    probabilities = model.predict_proba(features_df)[0]
    
    winning_team_prob = probabilities[prediction]

    return jsonify({
        'prediction': 'Blue Team Wins' if prediction == 1 else 'Red Team Wins',
        'winning_team_probability': winning_team_prob
    })

if __name__ == '__main__':
    app.run(debug=True)
