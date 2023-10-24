import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the movie data
movies_df = pd.read_csv(r"C:\Users\RISHU\OneDrive\Desktop\Python Coding\movies.csv")

# Clean and preprocess the data
movies_df = movies_df.drop_duplicates()
movies_df = movies_df.dropna()
movies_df = pd.get_dummies(movies_df, columns=["genre"])

# Split the data into training and testing sets
X = movies_df.drop(["success_score"], axis=1)
y = movies_df["success_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
