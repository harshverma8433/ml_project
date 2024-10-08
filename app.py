from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import dotenv
from dotenv import load_dotenv

load_dotenv()
application = Flask(__name__)
app = application

@app.route('/')
def index():
    print("fjkef")
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Extracting data from the form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        
        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        
        # Predict using pipeline
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Return the result in the rendered template
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))  # Default to port 5000 if not set in .env
    app.run(host="0.0.0.0", port=port, debug=True)