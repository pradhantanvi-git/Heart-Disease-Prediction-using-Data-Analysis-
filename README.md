# Heart Disease Prediction System using Machine Learning

## Overview
This project is a **Heart Disease Prediction System** developed using **Machine Learning algorithms** to assess the likelihood of heart disease in patients. It is implemented as a **web-based application** where users input their medical parameters, and the system predicts their risk level. The application integrates multiple **ML models**, including:
- **Decision Tree**
- **Logistic Regression**
- **Naïve Bayes**
- **Support Vector Classifier (SVC)**

The goal is to assist healthcare professionals and individuals in identifying potential heart disease risks based on key medical attributes.

## Authors & Contributors
- **Tanvi Pradhan**
- **Abhishek Singh**
- **Dhruva Trivedi**
- **Under the Guidance of:** *Dr. Bijith Marakarkandy* (HOD, I.T Department, TCET)

## Features
- **User Authentication:** Secure user registration and login system.
- **Machine Learning Models:** Implements Decision Tree, Logistic Regression, Naïve Bayes, and SVC.
- **Database Integration:** Stores user information and prediction results using SQLite.
- **Interactive Web Interface:** Developed using Flask with HTML/CSS frontend.
- **Medical Data Analysis:** Analyzes patient data, including Age, Cholesterol, Blood Pressure, etc.
- **Prediction Results:** Displays risk probability and allows users to take further action.
- **Doctor Consultation Module:** Redirects users to online doctor consultation platforms.

## Technologies Used
### **Programming & Frameworks**
- **Python** (Flask, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn)
- **HTML/CSS, Bootstrap** (for frontend UI)
- **Flask-SQLAlchemy** (Database Management)
- **Joblib & Pickle** (Model Serialization)
- **Matplotlib & Seaborn** (Data Visualization)

### **Machine Learning Models**
- **Decision Tree Classifier**
- **Logistic Regression**
- **Naïve Bayes Classifier**
- **Support Vector Classifier (SVC)**

## How It Works
1. **User Registration/Login**: Users create an account or log in.
2. **Input Medical Parameters**: Enter details such as age, cholesterol, BP, etc.
3. **Model Prediction**: The system runs inputs through ML models to generate results.
4. **Results Page**: Displays prediction result (Heart Disease: Yes/No).
5. **Consultation Module**: Redirects users to online doctor consultation if needed.

## Dataset Description
The dataset (`heart.csv`) consists of **14 attributes** related to heart health:
- **Age**
- **Sex**
- **Chest Pain Type (cp)**
- **Resting Blood Pressure (trestbps)**
- **Serum Cholesterol (chol)**
- **Fasting Blood Sugar (fbs)**
- **Resting ECG (restecg)**
- **Max Heart Rate Achieved (thalach)**
- **Exercise Induced Angina (exang)**
- **ST Depression (oldpeak)**
- **Slope of Peak Exercise ST Segment (slope)**
- **Number of Major Vessels (ca)**
- **Thalassemia (thal)**
- **Target**: (1 = Disease, 0 = No Disease)

## Machine Learning Model Performance
The models have been trained on the dataset to predict heart disease:

| Model                | Accuracy |
|----------------------|----------|
| **Decision Tree**    | ~85%     |
| **Logistic Regression** | ~87%  |
| **Naïve Bayes**      | ~84%     |
| **Support Vector Classifier (SVC)** | ~86% |

## Future Enhancements
- Implement **Deep Learning (Neural Networks)** for better accuracy.
- Deploy on **Cloud** for real-world accessibility.
- Develop a **Mobile Application** for easier usability.
- **Smart Wearable Device Integration** for real-time monitoring.

## License
This project is developed for **academic purposes** and is **open-source**.

---

**© 2021 Thakur College of Engineering & Technology**

