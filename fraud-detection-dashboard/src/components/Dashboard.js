// Dashboard.js
import React, { useState } from 'react';
import InputForm from './InputForm';
import PredictionChart from './PredictionChart';

const Dashboard = () => {
  const [predictions, setPredictions] = useState([]);

  const handlePrediction = (data) => {
    // Make API call to Flask backend with data
    const prediction = Math.random() > 0.5 ? 'Fraudulent' : 'Non-Fraudulent';
    // Update prediction state
    setPredictions([...predictions,prediction /* Prediction result from API call */]);
  };

  return (
    <div className="dashboard">
      <h1>Futuristic Fraud Detection Dashboard</h1>
      <InputForm onPrediction={handlePrediction} />
      <PredictionChart predictions={predictions} />
    </div>
  );
};

export default Dashboard;
