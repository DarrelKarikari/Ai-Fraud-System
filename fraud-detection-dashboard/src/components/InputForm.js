import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css'; // Import CSS file

const InputForm = ({ onPrediction }) => {
  const [date, setDate] = useState(new Date());
  const [amount, setAmount] = useState(0);
  const [feature1, setFeature1] = useState(0);
  const [feature2, setFeature2] = useState(0);
  const [feature3, setFeature3] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    const formattedDate = date.toLocaleDateString(); // Format date
    const data = {
      Date: formattedDate,
      Amount: amount,
      Feature1: feature1,
      Feature2: feature2,
      Feature3: feature3,
    };
    onPrediction(data);
  };

  return (
    <div className="input-form">
      <h2>Input Transaction Data</h2>
      <form onSubmit={handleSubmit}>
        <label>Date:</label>
        <DatePicker selected={date} onChange={(date) => setDate(date)} />
        <label>Amount:</label>
        <input type="number" value={amount} onChange={(e) => setAmount(parseFloat(e.target.value))} min={0} step={0.01} />
        <label>Feature 1:</label>
        <input type="number" value={feature1} onChange={(e) => setFeature1(parseFloat(e.target.value))} min={0} />
        <label>Feature 2:</label>
        <input type="number" value={feature2} onChange={(e) => setFeature2(parseFloat(e.target.value))} min={0} />
        <label>Feature 3:</label>
        <input type="number" value={feature3} onChange={(e) => setFeature3(parseFloat(e.target.value))} min={0} />
        <button type="submit">Predict</button>
      </form>
    </div>
  );
};

export default InputForm;
