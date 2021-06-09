import json
from tensorflow import keras
import numpy as np
from PIL import Image


model = keras.models.load_model(r'./pariii')

def get_label(x):
    """getting label from list of ML Model classes"""

    label = ['blas','hawar daun','titik coklat','sehat','hispa','tungro']
    predicted_label = label[x]
    return predicted_label

def predict(data):
    """Predict an image using loaded ML model returning json with label and probability percentage"""

    predicted_data = model.predict(data, batch_size=10)
    result = np.argmax(predicted_data[0])
    predicted_label = get_label(result)

    #Process prediction output into json format
    probability = int(np.max(predicted_data) * 100)
    probability = str(probability) + "%"
    jsonDict = {
        'label': predicted_label,
        'probability': probability
    }
    return json.dumps(jsonDict)

def process_img(data):
    """Processing image from HTTP POST into data for prediction"""

    image = Image.open(data).convert('RGB')
    resized_img = image.resize((256, 256))
    array_img = np.array(resized_img)
    expanded_array = np.expand_dims(array_img,  axis=0)
    processed_data = np.vstack([expanded_array])
    return processed_data
