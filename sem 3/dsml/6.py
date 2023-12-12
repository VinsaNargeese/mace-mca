import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

# Load Breast Cancer dataset
cancer_data = load_breast_cancer()
data = pd.DataFrame(np.c_[cancer_data['data'], cancer_data['target']], columns=np.append(cancer_data['feature_names'], ['target']))
data['target'] = data['target'].astype(int).astype('category')

# (i) Exploratory Data Analysis
eda_report = data.describe()

# (ii) Visualization for 'mean radius' feature
# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='mean radius', y='mean texture', hue='target', data=data, palette='viridis')
plt.title('Scatter Plot for Mean Radius vs. Mean Texture')
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='mean radius', bins=20, kde=True)
plt.title('Histogram for Mean Radius')
plt.show()

# Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='target', y='mean radius', data=data)
plt.title('Box Plot for Mean Radius by Target')
plt.show()

# (iii) Naïve Bayes Classification
# Prepare the data
X = data[['mean radius']]
y = data['target']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Implement Naïve Bayes Classification
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# Make predictions
y_pred = naive_bayes.predict(X_test)

# Display accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print('\nClassification Report:')
print(classification_rep)
print(f'Accuracy: {accuracy:.4f}')
