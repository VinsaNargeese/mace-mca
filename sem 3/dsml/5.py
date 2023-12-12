import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the Iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# (i) Exploratory Data Analysis
eda_report = df.describe()

# (ii) Visualization
# Scatter Plot
sns.pairplot(df, hue='target', palette='viridis')
plt.suptitle('Scatter Plot for Iris Dataset')
plt.show()

# Histogram
df[data.feature_names].hist(bins=20, figsize=(15, 10))
plt.suptitle('Histograms for Iris Dataset')
plt.show()

# Box Plot
plt.figure(figsize=(15, 10))
sns.boxplot(x='target', y='sepal length (cm)', data=df)
plt.title('Box Plot for Sepal Length by Target')
plt.show()

# (iii) Multiple Linear Regression
# Prepare the data
X = df[data.feature_names]
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Implement Multiple Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'\nMean Squared Error: {mse:.4f}')
print(f'R-squared: {r2:.4f}')
