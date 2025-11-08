import streamlit as st
import os
import sys

python_exe = sys.executable
os.environ["PYSPARK_PYTHON"] = python_exe
os.environ["PYSPARK_DRIVER_PYTHON"] = python_exe

from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

spark = SparkSession.builder \
    .appName("AttritionApp") \
    .master("local[1]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(os.path.dirname(current_dir), "models", "best_pipeline_model")
model = PipelineModel.load(model_path)

st.title("Prédiction Attrition Bancaire")

credit_score = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 30)
tenure = st.number_input("Ancienneté", 0, 10, 3)
balance = st.number_input("Solde", 0.0, 300000.0, 50000.0)
num_products = st.number_input("Nb produits", 1, 5, 2)
has_card = st.selectbox("Carte crédit", [0, 1])
is_active = st.selectbox("Membre actif", [0, 1])
salary = st.number_input("Salaire", 0.0, 200000.0, 50000.0)
geography = st.selectbox("Pays", ["France", "Germany", "Spain"])
gender = st.selectbox("Genre", ["Male", "Female"])

if st.button("Prédire"):
    gender_encoded = 1.0 if gender == "Male" else 0.0
    geo_france = 1 if geography == "France" else 0
    geo_germany = 1 if geography == "Germany" else 0
    geo_spain = 1 if geography == "Spain" else 0
    
    input_data = [[credit_score, age, tenure, balance, num_products, has_card, is_active, salary, 0, gender_encoded, geo_france, geo_germany, geo_spain]]
    columns = ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary", "Exited", "gender", "Geography_France", "Geography_Germany", "Geography_Spain"]
    
    input_df = spark.createDataFrame(input_data, columns)
    result = model.transform(input_df).collect()[0]
    prediction = result["prediction"]
    probability = result["probability"][int(prediction)]
    
    if prediction == 1.0:
        st.write(f"Client va partir (Probabilité: {probability:.1%})")
    else:
        st.write(f"Client reste (Probabilité: {probability:.1%})")
