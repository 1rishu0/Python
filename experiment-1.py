import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data from CSV file
data = pd.read_csv('data.csv')

# Extract X and y data
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the values using the trained model
y_pred = regressor.predict(X_test)

# Plot the training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Training Set')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Plot the test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Test Set')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
