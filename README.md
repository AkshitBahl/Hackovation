# Health Management System

HealthBuddy is a comprehensive healthcare application that makes online medical services seamless, accurate, fast and reliable. HealthBuddy aims at creating an ecosystem which makes healthcare accessible to everyone.

## Technologies Used

HealthBuddy is built on a robust technology stack designed for scalability and user-friendliness. This includes:

### Frontend:

1.HTML
2.CSS
3.JS

### Backend

1. Django

### Database

1. SQLite3

### Machine Learning

1. KMeans
2. RandomForestClassifier
3. Light GBM
4. DecisionTreesClassifier


## Useful Features:

1. AI-Powered Diagnosis: HealthBuddy leverages machine learning algorithms to analyze patient data and provide accurate diagnoses.
2. Personalized Prescription plans: Based on individual health profiles, the app generates personalized treatment plans.
3. Remote Appointment booking: The app automates appointment booking for patients to their nearby doctors.
4. Medical Chat-bot: LLM Bot-press chatbot to assist patients
   

### HealthBuddy stands out by combining three essential health tools into one seamless platform: 

1. a personalized Diet Planner,
2. an intelligent Insurance Predictor, and
3. an advanced Disease Predictor. 

This integration provides users with a comprehensive, end-to-end healthcare solution that goes beyond typical medical services.


## Prerequisites

Before you begin, ensure you have the following installed on your system:
* [Python 3.8+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
* [Git](https://git-scm.com/downloads/)

## 🚀 How to Run This Application

Follow these steps to get your development environment set up and running.


```bash
git clone https://github.com/AkshitBahl/Hackovation.git
cd Hackovation

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt django pandas scikit-learn
python manage.py migrate
python manage.py runserver
