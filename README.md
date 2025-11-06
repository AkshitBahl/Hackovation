# [Patient Registration System]

(Add a brief, 1-2 sentence description of what this project does. For example: "A simple web application built with Django for managing new patient registrations.")

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
