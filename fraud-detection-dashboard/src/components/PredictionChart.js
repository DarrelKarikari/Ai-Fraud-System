// PredictionChart.js
import React from 'react';
import { Line } from 'react-chartjs-2';

const PredictionChart = ({ predictions }) => {
  const data = {
    labels: predictions.map((_, index) => index + 1),
    datasets: [
      {
        label: 'Fraud Prediction',
        data: predictions,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div className="prediction-chart">
      <h2>Prediction Chart</h2>
      <Line data={data} />
    </div>
  );
};

export default PredictionChart;
