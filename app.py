import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('sales_model.pkl', 'rb'))

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives input values from the form,
    makes a prediction, and returns the result to the page.
    """
    # Get the input values from the form, convert them to float
    features = [float(x) for x in request.form.values()]

    # Reshape the features for a single prediction
    final_features = np.array(features).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(final_features)

    # Format the output to two decimal places
    output = round(prediction[0], 2)

    # Create the prediction text to be displayed on the page
    # Assuming the sales are in thousands of units/dollars
    prediction_text = f'Predicted Sales: {output} units'

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)