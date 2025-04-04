import kagglehub
import pandas as pd
import os

# Download Kaggle dataset
dataset_dir = kagglehub.dataset_download("uciml/pima-indians-diabetes-database")


data = pd.read_csv(/root/.cache/kagglehub/datasets/uciml/pima-indians-diabetes-database/versions/1/diabetes.csv)
print(data.head())
print(data.info())

print(data.columns)

import numpy as np

#Cleaning data
cols_with_zeroes = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
data[cols_with_zeroes] = data[cols_with_zeroes].replace(0, np.nan)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
data[cols_with_zeroes] = imputer.fit_transform(data[cols_with_zeroes])

#Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(data.drop('Outcome', axis=1))
data_scaled = pd.DataFrame(scaled_features, columns=data.columns[:-1])
data_scaled['Outcome'] = data['Outcome']

#Outliers
from scipy.stats import zscore
z_scores = np.abs(zscore(data_scaled.drop('Outcome', axis=1)))
data_cleaned = data_scaled[(z_scores < 3).all(axis=1)]
print(f"Data shape after outlier removal: {data_cleaned.shape}")

#Exploratory Data Analysis
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram for glucose distribution by outcome
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Glucose', hue='Outcome', multiple="dodge", bins=30)
plt.title('Glucose Levels by Diabetes Outcome')
plt.xlabel('Glucose')
plt.ylabel('Count')
plt.show()

# Correlation matrix
corr_matrix = data.drop('Outcome', axis=1).corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm',
            vmin=-1, vmax=1,
            center=0)
plt.title('Feature Correlation Heatmap')
plt.show()

#Modeling ; split data
from sklearn.model_selection import train_test_split
X = data_cleaned.drop('Outcome', axis=1)
y = data_cleaned['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# SVM
svm = SVC(probability=True)
svm.fit(X_train, y_train)

#Hyperparameter tuning
from sklearn.model_selection import GridSearchCV

# Tuning KNN
knn_params = {'n_neighbors': [3, 5, 7, 9]}
grid_knn = GridSearchCV(KNeighborsClassifier(), knn_params, cv=5)
grid_knn.fit(X_train, y_train)

print(f"Best KNN parameters: {grid_knn.best_params_}")

#Model evaluation
from sklearn.metrics import classification_report, roc_auc_score

for model, name in zip([lr, knn, svm], ["Logistic Regression", "KNN", "SVM"]):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    print(f"Model: {name}")
    print(classification_report(y_test, y_pred))
    print(f"AUC: {roc_auc_score(y_test, y_proba)}\n")

#plot roc curves
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

models = [("Logistic Regression", lr), ("KNN", knn), ("SVM", svm)]
plt.figure(figsize=(8, 6))

for name, model in models:
    fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
    plt.plot(fpr, tpr, label=name)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves")
plt.legend()
plt.show()
