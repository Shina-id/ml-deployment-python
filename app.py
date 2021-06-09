from flask import Flask, request
import paddy

app = Flask(__name__)

@app.route('/')
def hello():
    return 'USE path /api/predict to predict image with POST method'

@app.route('/api/predict', methods=['POST'])
def predict_image():
    image = request.files['image']
    processed_data = paddy.process_img(image)
    jsonResponse = paddy.predict(processed_data)
    return jsonResponse

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
