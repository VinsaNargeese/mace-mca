import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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

# (iii) K-Means Clustering
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[data.feature_names])

# Implement K-Means with different K values
k_values = [2, 3, 4]
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  # Explicitly set n_init
    df['cluster'] = kmeans.fit_predict(X_scaled)

    # Print the centroids
    centroids = kmeans.cluster_centers_
    print(f'\nCentroids for k={k}:\n{centroids}')

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='cluster', data=df, palette='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red', label='Centroids')
    plt.title(f'K-Means Clustering (k={k}) with Centroids')
    plt.legend()
    plt.show()
