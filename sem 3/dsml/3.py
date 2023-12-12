import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load the Breast Cancer dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# (i) Exploratory Data Analysis
# Statistical analysis
info_report = df.info()
head_report = df.head()
describe_report = df.describe()

# Mean and Mode of the target variable
target_mean = df['target'].mean()
target_mode = df['target'].mode().values[0]

print(f"\nMean of the target variable (diagnosis): {target_mean:.4f}")
print(f"Mode of the target variable (diagnosis): {target_mode}")

# (ii) Visualization
# Scatter Plot
sns.pairplot(df, hue='target', vars=data.feature_names[:5])  # Adjust vars parameter as needed
plt.suptitle('Scatter Plot for Breast Cancer Dataset')
plt.show()

# Histogram
df[data.feature_names].hist(bins=20, figsize=(15, 10))
plt.suptitle('Histograms for Breast Cancer Dataset')
plt.show()

# Box Plot
plt.figure(figsize=(15, 10))
sns.boxplot(x='target', y='mean radius', data=df)
plt.title('Box Plot for mean radius by Target')
plt.show()

# (iii) k-NN Classification
X_train, X_test, y_train, y_test = train_test_split(df[data.feature_names], df['target'], test_size=0.2, random_state=42)

# Implement k-NN with different k values
k_values = [3, 5, 7]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f'\nAccuracy for k={k}: {accuracy:.4f}')

# Print statistical analysis
print("\nInformation about the dataset:")
print(info_report)
print("\nFirst few rows of the dataset:")
print(head_report)
print("\nStatistical summary of the dataset:")
print(describe_report)
