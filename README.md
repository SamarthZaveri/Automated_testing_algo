📌 Project Overview

This project implements a structured pipeline for automated data collection, preprocessing, and machine learning model training.
It has been developed to demonstrate practical skills in Python programming, data analysis, and applied ML/AI techniques.

The system is modular and consists of the following components:

data_fetcher.py → Fetches financial market data using the yfinance API.

data_processor.py → Cleans, normalizes, and prepares data for analysis.

model_trainer.py → Trains and evaluates a predictive machine learning model using scikit-learn.

main.py → Integrates all modules into an end-to-end workflow.

Installation

Clone the repository and set up the environment:

git clone https://github.com/YOUR_USERNAME/Automated_Testing.git
cd Automated_Testing

# (Optional but recommended: create a virtual environment)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

Usage

Execute the pipeline with:

python main.py


This will:

Retrieve stock data (default: AAPL).

Process and prepare the dataset.

Train a machine learning model.

Display predictions and evaluation metrics.

Project Structure
Automated_Testing/
│── data_fetcher.py     # Data retrieval module
│── data_processor.py   # Data cleaning and preprocessing
│── model_trainer.py    # Model training and evaluation
│── main.py             # Orchestration script
│── requirements.txt    # List of dependencies
│── README.md           # Documentation

Technologies Used

Python 3.10+

yfinance → Market data collection

pandas, numpy → Data manipulation

scikit-learn → Machine learning

gspread, oauth2client → Google Sheets integration (optional)
