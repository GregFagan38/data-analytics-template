import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a sample dataset for demonstration
np.random.seed(42)
data = pd.DataFrame({
    'feature_1': np.random.normal(50, 15, 1000),  # Normal distribution
    'feature_2': np.random.uniform(10, 100, 1000),  # Uniform distribution
    'feature_3': np.random.binomial(1, 0.5, 1000)  # Binary feature
})

# Set up the figure and axis
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Plot 1: Histogram for feature_1
sns.histplot(data['feature_1'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Distribution of Feature 1')

# Plot 2: Histogram for feature_2
sns.histplot(data['feature_2'], kde=True, ax=axes[0, 1], color='orange')
axes[0, 1].set_title('Distribution of Feature 2')

# Plot 3: Histogram for feature_3
sns.histplot(data['feature_3'], kde=True, ax=axes[0, 2], color='green')
axes[0, 2].set_title('Distribution of Feature 3')

# Plot 4: Boxplot for feature_1
sns.boxplot(x=data['feature_1'], ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Boxplot of Feature 1')

# Plot 5: Boxplot for feature_2
sns.boxplot(x=data['feature_2'], ax=axes[1, 1], color='orange')
axes[1, 1].set_title('Boxplot of Feature 2')

# Plot 6: Correlation heatmap
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1, 2])
axes[1, 2].set_title('Correlation Heatmap')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the figure as a PNG file
plt.savefig('data_overview.png')

# Show the plot (optional)
plt.show()
