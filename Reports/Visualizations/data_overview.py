import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a sample dataset for demonstration
np.random.seed(42)
data = pd.DataFrame({
    'feature_1': np.random.normal(50, 15, 1000),  # Normal distribution
    'feature_2': np.random.uniform(10, 100, 1000),  # Uniform distribution
    'feature_3': np.random.binomial(1, 0.5, 1000),  # Binary feature
    'feature_4': np.random.normal(30, 10, 1000)   # Another Normal distribution
})

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Generate the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Title and labels
plt.title('Correlation Heatmap of Features')
plt.tight_layout()

# Save the heatmap as a PNG file
plt.savefig('correlation_heatmap.png')

# Show the plot (optional)
plt.show()
