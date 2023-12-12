import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the Wine Quality dataset
wine_data = pd.read_csv('/home/user/PycharmProjects/1/WineQuality - WineQuality.csv')

# (i) Exploratory Data Analysis
eda_report = wine_data.describe()

# (ii) Visualization for 'alcohol' feature
# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='alcohol', y='quality', data=wine_data)
plt.title('Scatter Plot for Alcohol Content by Quality')
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data=wine_data, x='alcohol', bins=20, kde=True)
plt.title('Histogram for Alcohol Content')
plt.show()

# Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=wine_data)
plt.title('Box Plot for Alcohol Content by Quality')
plt.show()

# (iii) k-NN Classification
# Prepare the data
X = wine_data[['alcohol']]
y = wine_data['quality']

# Create a pipeline with k-NN classification
pipeline = Pipeline([
    ('classifier', KNeighborsClassifier(n_neighbors=5))  # Example k value, adjust as needed
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Display accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, zero_division=1)  # Setting zero_division to 1

print(f'\nAccuracy: {accuracy:.4f}')
print(f'Classification Report:\n{classification_rep}')
