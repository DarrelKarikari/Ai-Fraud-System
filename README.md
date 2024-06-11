<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Futuristic Fraud Detection System</h1>

<h2>Overview</h2>

<p>The Futuristic Fraud Detection System is a web application designed to detect fraudulent transactions using advanced machine learning algorithms. It consists of both backend and frontend components, providing a seamless user experience for inputting transaction data and visualizing fraud predictions.</p>

<h2>Backend Features</h2>

<ol>
  <li>
    <h3>Data Preprocessing</h3>
    <ul>
      <li><strong>Load and Preprocess Data:</strong> Preprocesses transaction data by loading CSV files, handling missing values, scaling numerical features, and oversampling using SMOTE to address class imbalance.</li>
      <li><strong>Advanced Feature Engineering:</strong> Enhances data by adding advanced features like polynomial features and NLP features to improve model performance.</li>
    </ul>
  </li>
  <li>
    <h3>Model Training</h3>
    <ul>
      <li><strong>Gradient Boosting Classifier:</strong> Trains a Gradient Boosting Classifier using grid search for hyperparameter tuning.</li>
      <li><strong>Model Evaluation:</strong> Evaluates model performance using metrics like ROC-AUC score and classification report.</li>
    </ul>
  </li>
  <li>
    <h3>Flask API</h3>
    <ul>
      <li><strong>RESTful API:</strong> Provides a Flask API for making predictions on new transaction data.</li>
      <li><strong>API Endpoints:</strong> Exposes endpoints for predicting fraud probabilities and integrating with the frontend.</li>
    </ul>
  </li>
</ol>

<h2>Frontend Features</h2>

<ol>
  <li>
    <h3>User Interface</h3>
    <ul>
      <li><strong>Input Transaction Data:</strong> Allows users to input transaction data, including date, amount, and various features.</li>
      <li><strong>Prediction Chart:</strong> Visualizes fraud predictions using a line chart to display the probability of fraud over time.</li>
    </ul>
  </li>
  <li>
    <h3>Navigation</h3>
    <ul>
      <li><strong>Navbar:</strong> Provides navigation links to different pages, including the dashboard, about page, and contact page.</li>
    </ul>
  </li>
  <li>
    <h3>Error Handling</h3>
    <ul>
      <li><strong>Not Found Page:</strong> Displays a 404 page when users navigate to non-existing routes, providing a user-friendly error message.</li>
    </ul>
  </li>
</ol>

<h2>Technologies Used</h2>

<h3>Backend</h3>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>scikit-learn</li>
  <li>imbalanced-learn</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>React</li>
  <li>React Router</li>
  <li>Chart.js</li>
  <li>react-datepicker</li>
</ul>

<h2>Setup Instructions</h2>

<ol>
  <li><strong>Backend Setup</strong>:
    <ul>
      <li>Install Python dependencies using <code>pip install -r requirements.txt</code>.</li>
      <li>Run the Flask server using <code>python app.py</code>.</li>
    </ul>
  </li>
  <li><strong>Frontend Setup</strong>:
    <ul>
      <li>Install Node.js dependencies using <code>npm install</code>.</li>
      <li>Start the development server using <code>npm start</code>.</li>
    </ul>
  </li>
  <li><strong>Accessing the Application</strong>:
    <ul>
      <li>Open the browser and navigate to <code>http://localhost:3000</code> to access the frontend dashboard.</li>
    </ul>
  </li>
</ol>

<h2>Future Enhancements</h2>

<ul>
  <li>Implement user authentication and authorization for secure access to the application.</li>
  <li>Enhance the frontend UI with additional features like data visualization and user interactions.</li>
  <li>Deploy the application to production servers for real-world usage.</li>
</ul>



<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

</body>
</html>
