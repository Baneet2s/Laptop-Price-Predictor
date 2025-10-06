# Laptop Price Predictor

A web-based machine learning tool that predicts the market value of laptops based on their specifications. This project leverages a complete data science workflow, from data cleaning and model training to deployment as a containerized web application.

---

### 📌 Problem Statement

The laptop market is saturated with a vast array of models, brands, and configurations, making it difficult for consumers to gauge fair market prices. Manually comparing specifications is time-consuming and often inconclusive. This project aims to solve this by creating an intelligent tool that provides instant, data-driven price estimates, empowering users to make informed purchasing decisions.

### My Contributions

As the sole developer on this project, I was responsible for the end-to-end development lifecycle:

* **Data Engineering**: Performed extensive data cleaning, preprocessing, and feature engineering on a raw dataset of over 1300 laptops to prepare it for modeling. This included handling missing values, extracting key information from text (e.g., CPU brand, GPU brand), and creating new features like PPI (Pixels Per Inch).
* **Machine Learning Modeling**: Selected, trained, and evaluated several regression models. A `RandomForestRegressor` was chosen as the final model due to its high performance and robustness. I built a `scikit-learn` pipeline to streamline the preprocessing and prediction workflow.
* **Backend Development**: Built a lightweight and efficient web server using **Flask** to handle user requests, process inputs, and serve model predictions.
* **Frontend Development**: Designed a simple, responsive, and user-friendly interface with **HTML** and **Bootstrap** to ensure a smooth user experience.
* **Containerization**: Wrote a **Dockerfile** to containerize the entire Flask application, including all dependencies and the trained model, ensuring easy and reproducible deployment.

### 🛠️ Technical Skills Used

* **Languages**: Python
* **Libraries**: Scikit-learn, Pandas, NumPy
* **Web Framework**: Flask
* **Frontend**: HTML, Bootstrap
* **Deployment**: Docker

### ✅ Results & Outcome

* **High Accuracy**: The final prediction model achieved an **R² score of over 75%** on the test dataset, indicating a strong correlation between the predicted prices and actual market values.
* **Functional Web Application**: Successfully developed and deployed a fully functional web application where users can select laptop specifications and receive an instant price prediction.
* **Strategic Insights**: The model's feature importance analysis revealed that factors like RAM, SSD capacity, and CPU brand have the most significant impact on laptop pricing.

### 🧠 Problems Faced & Solutions

* **Problem**: The raw dataset contained noisy and inconsistent categorical data (e.g., over 50 unique CPU entries).
    * **Solution**: I engineered new features by extracting the core brand (e.g., 'Intel', 'AMD') from the detailed strings, simplifying the feature space and improving model performance. One-hot encoding was then applied to handle these categorical features effectively.
* **Problem**: Ensuring the application could run consistently across different machines without dependency conflicts.
    * **Solution**: I used Docker to create a self-contained image of the application. This encapsulated the Python environment, Flask server, and all necessary files, making deployment reliable and straightforward.

### 🚀 Future Enhancements

* **Incorporate More Data**: Integrate additional data points like brand reputation scores, user reviews, and regional sales trends to capture more market nuances.
* **Dynamic Price Updates**: Implement a mechanism to connect to live e-commerce APIs, allowing the model to adjust its predictions based on real-time market fluctuations.
* **Explore Deep Learning**: For a larger and more complex dataset, experimenting with neural network models could potentially uncover more intricate patterns and further improve prediction accuracy.
