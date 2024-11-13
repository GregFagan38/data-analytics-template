import matplotlib.pyplot as plt
import numpy as np

# Example model performance metrics (replace with actual values from your model)
metrics = {
    'Accuracy': 0.85,
    'Precision': 0.80,
    'Recall': 0.75,
    'F1 Score': 0.77
}

# Set up the figure
plt.figure(figsize=(8, 6))

# Bar plot of the model metrics
plt.bar(metrics.keys(), metrics.values(), color=['skyblue', 'orange', 'green', 'red'])

# Title and labels
plt.title('Model Performance Metrics', fontsize=16)
plt.ylabel('Score', fontsize=12)
plt.ylim(0, 1)  # Score is between 0 and 1

# Add the score values above each bar
for i, v in enumerate(metrics.values()):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center', fontsize=12)

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('model_performance.png')

# Show the plot (optional)
plt.show()
