# Author: Priti Gupta
# Date: June 15th, 2023
# Description: Scrapping data from glassdoor to analyse salaries of data science positions in India
# GitHub: https://github.com/PritiG1/DS-SalaryPredictor

import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open('regression_model_ds.pkl', 'rb'))

@app.route("/")
def Home():
    return render_template("index.html")

# Define a route for the prediction endpoint
@app.route('/predict', methods=["POST"])
def predict():
    experience = float(request.form['Experience (yrs)'])  # Get the experience value from the form
    prediction = model.predict([[experience]])  # Make predictions using the loaded model

    return render_template("index.html", prediction_text="The estimated salary for a data scientist with {} years of experience is {} Lacs".format(experience, np.round(prediction,2)))

# Run the app if executed directly
if __name__ == "__main__":
    app.run(debug=True)