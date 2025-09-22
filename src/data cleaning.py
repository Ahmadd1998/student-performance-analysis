# 2. FEATURE ENGINEERING
print("FEATURE ENGINEERING")

# Check Duplicated Data
duplicates = dataset.duplicated().sum()
print(f"Number of duplicated rows: {duplicates}")

# Check Missing Values
missing_values = dataset.isnull().sum()
print(f"Missing values:\n{missing_values}")

# Outlier Analysis
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=dataset['Hours'])
plt.title('Box Plot of Hours Studied')

plt.subplot(1, 2, 2)
sns.boxplot(y=dataset['Scores'])
plt.title('Box Plot of Scores')

plt.tight_layout()
plt.show()
