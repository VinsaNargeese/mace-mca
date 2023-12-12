# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt

# Load the Winequality dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
wine_data = pd.read_csv(url, sep=';')

# Check if the 'color' column exists in the dataset
if 'color' in wine_data.columns:
    # Convert the 'color' column to numerical values using one-hot encoding
    wine_data = pd.get_dummies(wine_data, columns=['color'], drop_first=True)

# Separate features (X) and target variable (y)
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier with max_depth to prune the tree
dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=3)

# Train the model
dt_classifier.fit(X_train, y_train)

# (v) Classification Report
y_pred = dt_classifier.predict(X_test)
classification_rep = classification_report(y_test, y_pred, zero_division=1)
print("Classification Report:")
print(classification_rep)


# (vi) Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)

# (vii) Plot Pruned Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(dt_classifier, feature_names=X.columns, class_names=[str(label) for label in dt_classifier.classes_], filled=True, rounded=True)
plt.show()
