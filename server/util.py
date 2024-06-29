import pickle
import numpy as np
import pandas as pd
import sklearn.preprocessing as MinMaxScaler

__model = None

def get_game_prediction(blueFirstBlood, blueKills, blueDeaths, blueAssists, blueDragons, blueTowersDestroyed, blueGoldDiff, blueExperienceDiff, redAssists, redDragons, redTowersDestroyed):
    df = pd.DataFrame({
        'blueFirstBlood': [blueFirstBlood],
        'blueKills': [blueKills],
        'blueDeaths': [blueDeaths],
        'blueAssists': [blueAssists],
        'blueDragons': [blueDragons],
        'blueTowersDestroyed': [blueTowersDestroyed],
        'blueGoldDiff': [blueGoldDiff],
        'blueExperienceDiff': [blueExperienceDiff],
        'redAssists': [redAssists],
        'redDragons': [redDragons],
        'redTowersDestroyed': [redTowersDestroyed]
    })
    
    predicted_class = __model.predict(df)[0] 
    probabilities = __model.predict_proba(df)[0]  
    predicted_class_probability = probabilities[predicted_class]
    
    return predicted_class, predicted_class_probability

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __model
    if __model is None:
        with open("./server/artifacts/lol_model.pickle", 'rb') as f:
            __model = pickle.load(f)
            
    print("Loading saved artifacts...done")
                  
                  
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_game_prediction(1, 30, 5, 0, 0, 0, 2000, 200, 0, 0, 0))