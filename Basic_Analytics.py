import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "/Users/mohitkumar/Downloads/organizations-100.csv"  # CSV File Path
data = pd.read_csv(file_path)

# Perform basic data analysis
analysis_results = {}
for column in data.select_dtypes(include=np.number):  # Analyze numeric columns only
    mean_value = np.mean(data[column])
    median_value = np.median(data[column])
    mode_value = data[column].mode()[0]  # Get the first mode value
    
    analysis_results[column] = {
        "Mean": mean_value,
        "Median": median_value,
        "Mode": mode_value
    }

# Print analysis results
print("\nBasic Data Analysis:")
for column, stats in analysis_results.items():
    print(f"{column}:")
    for stat_name, value in stats.items():
        print(f"  {stat_name}: {value}")


# Plot the mean, median, and mode for each numeric column
for column in analysis_results.keys():
    stats = analysis_results[column]
    plt.figure(figsize=(6, 4))
    plt.bar(stats.keys(), stats.values(), color=['blue', 'orange', 'green'])
    plt.title(f"{column} - Mean, Median, Mode")
    plt.ylabel('Value')
    plt.xlabel('Statistic')
    plt.show()