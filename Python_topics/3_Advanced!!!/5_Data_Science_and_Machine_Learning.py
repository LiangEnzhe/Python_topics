# ----------------------------------------------------------------------
# Data Science and Machine Learning in Python
# ----------------------------------------------------------------------
# Python provides a rich ecosystem of libraries for data manipulation, visualization,
# and machine learning. Here, we'll focus on popular libraries:
# - `numpy`: For numerical computations.
# - `pandas`: For data manipulation and analysis.
# - `matplotlib`: For data visualization.
# - `scikit-learn`: For machine learning.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.cluster import KMeans

# ----------------------------------------------------------------------
# 1. Libraries Overview: numpy and pandas
# ----------------------------------------------------------------------

# a. Using `numpy` for numerical operations
data = np.array([1, 2, 3, 4, 5])
print("Array:", data)  # Prints: Array: [1 2 3 4 5]

# Perform operations
print("Mean:", np.mean(data))  # Prints: Mean: 3.0
print("Standard Deviation:", np.std(data))  # Prints: Standard Deviation: 1.414213562...

# b. Using `pandas` for data manipulation
# Create a DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
})

# Inspect the data
print(df.head())  # Prints the first few rows of the DataFrame
print(df.describe())  # Summary statistics of numeric columns

# Add a new column
df["Bonus"] = df["Salary"] * 0.1
print(df)

# Filter rows
filtered = df[df["Age"] > 28]
print(filtered)  # Prints rows where Age > 28

# ----------------------------------------------------------------------
# 2. Data Visualization with `matplotlib`
# ----------------------------------------------------------------------

# Create a simple line plot
plt.figure(figsize=(8, 5))
x = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
y = np.sin(x)
plt.plot(x, y, label="Sine Wave")
plt.title("Sine Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Salary"], color="red", label="Salaries")
plt.title("Salary vs Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()

# ----------------------------------------------------------------------
# 3. Machine Learning with `scikit-learn`
# ----------------------------------------------------------------------
# Scikit-learn provides tools for machine learning, including regression, classification,
# clustering, and preprocessing.

# ----------------------------------------------------------------------
# 3.1 Linear Regression
# ----------------------------------------------------------------------

# Generate synthetic data
X = np.random.rand(100, 1)  # 100 rows, 1 column
y = 3 * X[:, 0] + 5 + np.random.randn(100) * 0.5  # y = 3x + 5 + noise

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")  # Prints the MSE of the model
print(f"Model Coefficients: {model.coef_}, Intercept: {model.intercept_}")

# Visualize the results
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color="red", label="Predicted")
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# ----------------------------------------------------------------------
# 3.2 Classification (Logistic Regression)
# ----------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels (0, 1, 2)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
classifier = LogisticRegression(max_iter=200)
classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test)

# Evaluate the classifier
print(classification_report(y_test, y_pred))  # Prints precision, recall, F1-score

# ----------------------------------------------------------------------
# 3.3 Clustering (K-Means)
# ----------------------------------------------------------------------

# Generate synthetic data for clustering
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Train a K-Means clustering model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Plot the clusters
plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis", marker="o")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color="red", marker="x", s=200, label="Centroids")
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# ----------------------------------------------------------------------
# Summary: Data Science and Machine Learning with Python
# ----------------------------------------------------------------------

# 1. **Libraries**:
#    - `numpy`: For numerical computations.
#    - `pandas`: For data manipulation and analysis.
#    - `matplotlib`: For data visualization.
#    - `scikit-learn`: For machine learning.

# 2. **Data Wrangling and Visualization**:
#    - Use `pandas` for cleaning, filtering, and transforming data.
#    - Use `matplotlib` to visualize trends, patterns, and relationships in data.

# 3. **Machine Learning**:
#    - **Linear Regression**: Predict continuous values (e.g., housing prices).
#    - **Classification**: Categorize data points (e.g., classify flowers in the Iris dataset).
#    - **Clustering**: Group data points into clusters (e.g., K-Means for customer segmentation).

# Python’s ecosystem makes it a go-to choice for Data Science and Machine Learning tasks.
