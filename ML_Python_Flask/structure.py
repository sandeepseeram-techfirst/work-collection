from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Load input data
    input_data = request.json
    
    # Load model
    model = load_model()
    
    # Make predictions
    output_data = model.predict(input_data)
    
    # Return output data
    return jsonify(output_data.tolist())


if __name__ == '__main__':
    app.run(debug=True)
