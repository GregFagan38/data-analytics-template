# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up visualization style
sns.set(style="whitegrid")
%matplotlib inline

# Load the dataset
data = pd.read_csv('path_to_your_data.csv')

# Data overview
print("Data Overview:")
print(data.head())

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Data Cleaning (if necessary)
# Example: Fill missing values
data.fillna(data.mean(), inplace=True)

# Feature Engineering (if applicable)
# Example: Create a new feature
data['new_feature'] = data['feature_1'] * data['feature_2']

# Exploratory Data Analysis (EDA)
# Example: Histogram for a feature
plt.figure(figsize=(10, 6))
sns.histplot(data['feature_1'], kde=True, color='skyblue')
plt.title('Distribution of Feature 1')
plt.show()

# Model building (if applicable)
# Example: Train-test split and simple model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = data[['feature_1', 'feature_2']]
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
print("\nModel Evaluation:")
from sklearn.metrics import mean_squared_error
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Save model (optional)
import joblib
joblib.dump(model, 'model.pkl')

print("\nScript Completed!")
