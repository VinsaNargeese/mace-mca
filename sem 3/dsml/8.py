import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load Housing Price dataset
data = pd.read_csv('/home/user/PycharmProjects/1/venv/Housing - Housing.csv')

# (i) Exploratory Data Analysis
eda_report = data.describe()

# (ii) Visualization
# Scatter Plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='price', y='area', data=data, hue='furnishingstatus', palette='viridis')
plt.title('Scatter Plot for Feature1 vs. Feature2')
plt.show()

# Histogram
data.hist(bins=20, figsize=(15, 10))
plt.suptitle('Histograms for Housing Price Dataset')
plt.show()

# Box Plot
plt.figure(figsize=(15, 10))
sns.boxplot(x='furnishingstatus', y='price', data=data)
plt.title('Box Plot for Feature1 by Target')
plt.show()

# (iii) K-Means Clustering
# Prepare the data
X = data[['price', 'area']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Implement K-Means clustering for different k values
k_values = [2, 3, 4, 5]
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    data['cluster'] = kmeans.fit_predict(X_scaled)
    centroids = kmeans.cluster_centers_
    print(f'Centroids for k={k}:')
    print(centroids)

    accuracy = accuracy_score(data['furnishingstatus'], data['cluster'])
    # Visualize the clusters
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='price', y='area', data=data, hue='cluster', palette='viridis')
    plt.title(f'K-Means Clustering with k={k}, Accuracy={accuracy:.4f}')
    plt.show()
