import pandas as pd
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient
from azure.ai.ml import command

try:
    credential  = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except:
    credential = InteractiveBrowserCredential()

ml_client = MLClient.from_config(credential=credential)


print("Loading Data...")

data_sorvetes  = pd.read_csv("vendas_sorvetes.csv")

# Preparação dos Dados
X, y = data_sorvetes[['Temperatura']].values, data_sorvetes['Vendas'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

reg = 0.01

# Treinamento do Modelo

print("Training a logistic regression model with regularization rate of", reg)
modelo = LinearRegression(C=1/reg, solver='liblinear').fit(X_train, y_train)

# Calcula a acuracia
y_hat = modelo.predict(X_test)
acc = np.average(y_hat == y_test)
print("Accuracy:", acc)

# Calcula AUC
y_scores = modelo.predict_proba(X_test)
auc = roc_auc_score(y_test,y_scores[:,1])
print("AUC:", str(auc))

# Configure job

job = command(
    code = "./src",
    command = "python vendas_sovertes-training.py",
    environment = "AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute = "aml-cluster",
    display_name = "vendas-sorvertesv2-train",
    experiment_name = "vendas_sorvetes-training"
)

# Enviar job

returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url
print("Monitor your job at", aml_url)
