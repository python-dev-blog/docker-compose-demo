import React, { useState } from 'react';

const PredictionButton = () => {
  const [prediction, setPrediction] = useState('');

  const generatePrediction = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/prediction');
      const data = await response.json();
      setPrediction(data.prediction);
      console.log(data);
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

  return (
    <div className="prediction-button-container">
      <button onClick={generatePrediction} className="generate-button">
        Generate Your Prediction for Today
      </button>
      <div className="prediction">{prediction}</div>
    </div>
  );
};

export default PredictionButton;
