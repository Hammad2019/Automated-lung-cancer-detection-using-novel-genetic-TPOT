# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14YK_tu8wcEKOlUCfd1pQBRJU3R3kVMpq

## Load the dataset
"""

from google.colab import drive
drive.mount('/content/drive')

"""xray"""

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
# Load the combined_features.csv file
xray_df = pd.read_csv('/content/drive/MyDrive/Dataset_Dr_mohamed_task4/xray_features.csv')

# Separate features (X) and labels (y)
Xxray = xray_df.drop('label', axis=1)
yxray = xray_df['label']

"""chest ct"""

import pandas as pd
# Load the combined_features.csv file
chest_df = pd.read_csv('/content/drive/MyDrive/Dataset_Dr_mohamed_task4/chest_features.csv')
# Separate features (X) and labels (y)
Xchest = chest_df.drop('label', axis=1)
ychest = chest_df['label']

# Get the number of columns
num_columns = xray_df.shape[1]
print("Number of columns:", num_columns)
# Get the number of columns
num_columns = chest_df.shape[1]
print("Number of columns:", num_columns)

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Assuming xray_df and chest_df contain your feature dataframes

# Extract the labels from chest_df
ychest = chest_df['label'].values

# Convert values to desired labels
ychest = np.where(np.isin(ychest, [0, 1, 3]), 1, 0)

# Remove the existing 'labels' column from chest_df
chest_df = chest_df.drop(columns='label')

# Add the converted labels to chest_df as a new column
chest_df['label'] = ychest

# Merge the dataframes
combined_df = pd.concat([xray_df, chest_df], ignore_index=True)

# Shuffle the combined dataframe
shuffled_df = shuffle(combined_df, random_state=42)

# Get the number of columns in the shuffled dataframe
num_columns = shuffled_df.shape[1]
print("Number of columns:", num_columns)

"""

```
# This is formatted as code
```

# train test split"""

# Splitting into features (X) and labels (y)
X = shuffled_df.iloc[:, :num_columns-1]  # Assuming the labels are in the last column
y = shuffled_df.iloc[:, num_columns-1]

# Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# Calculate the minimum and maximum values
min_value = np.min(X_train)
max_value = np.max(X_train)

# Print the minimum and maximum values
print("Minimum value:", min_value)
print("Maximum value:", max_value)

from sklearn.preprocessing import MinMaxScaler

# Assuming X_train is the training data

# Create an instance of MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler on the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Print the minimum and maximum values of the scaled data
print("Minimum value of scaled data:", np.min(X_train_scaled))
print("Maximum value of scaled data:", np.max(X_train_scaled))

# Fit the scaler on the training data and transform it
X_test_scaled = scaler.fit_transform(X_test)

# Print the minimum and maximum values of the scaled data
print("Minimum value of scaled data:", np.min(X_test_scaled))
print("Maximum value of scaled data:", np.max(X_test_scaled))

from sklearn.preprocessing import LabelEncoder
# Convert the label data to string values
y_train_str = y_train.astype(str)
y_test_str = y_test.astype(str)
# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Fit the LabelEncoder on the training labels and transform them
y_train_encoded = label_encoder.fit_transform(y_train_str)

# Transform the test labels using the fitted LabelEncoder
y_test_encoded = label_encoder.transform(y_test_str)

# Print the encoded labels
print("Encoded training labels:", y_train_encoded)
print("Encoded test labels:", y_test_encoded)

import numpy as np

# Count the occurrences of the label '2' in the encoded training labels
count_train = np.sum(y_train_encoded == 2)

# Count the occurrences of the label '2' in the encoded test labels
count_test = np.sum(y_test_encoded == 2)

# Print the counts
print("Encoded count of label '2' in the training labels:", count_train)
print("Encoded count of label '2' in the test labels:", count_test)

# Find the indices of instances with label '2' in the training labels
indices_to_remove = np.where(y_train_encoded == 2)[0]

# Remove instances with label '2' from the training data and labels
X_train_filtered = np.delete(X_train_scaled, indices_to_remove, axis=0)
y_train_filtered = np.delete(y_train_encoded, indices_to_remove, axis=0)

# Print the updated shape of the filtered training data and labels
print("Updated shape of X_train_filtered:", X_train_filtered.shape)
print("Updated shape of y_train_filtered:", y_train_filtered.shape)

import numpy as np
# Count the occurrences of the label '2' in the encoded training labels
count_train = np.sum(X_train_filtered == 2)
# Print the counts
print("Encoded count of label '2' in the training labels:", count_train)

print(X_train_filtered.shape, y_train_filtered.shape)
print(X_test_scaled.shape, y_test_encoded.shape)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Assuming you have features and labels separated in X and y
X_combined = pd.DataFrame(np.concatenate([X_train_filtered, X_test_scaled], axis=0))
y_combined = pd.Series(np.concatenate([y_train_filtered, y_test_encoded], axis=0))

# Shuffle the combined data
combined_df = shuffle(pd.concat([X_combined, y_combined], axis=1), random_state=42)

# Set a Seaborn style
sns.set(style="whitegrid")

# Calculate class distribution for the combined dataset
combined_class_distribution = y_combined.value_counts()

# Print the shapes
print("Shapes:")
print("X_train_filtered:", X_train_filtered.shape)
print("y_train_filtered:", y_train_filtered.shape)
print("X_test_scaled:", X_test_scaled.shape)
print("y_test_encoded:", y_test_encoded.shape)

# Plot the distribution
fig, ax = plt.subplots(figsize=(8, 6))

# Plot for the combined dataset
colors = ['skyblue', 'lightcoral']  # Adjust colors if needed
bars = ax.bar(combined_class_distribution.index.astype(str), combined_class_distribution.values, color=colors)

# Set labels and title
ax.set_title('Class Distribution in the Combined Dataset', fontsize=16)
ax.set_xlabel('LUNG_CANCER Features')
ax.set_ylabel('Count', fontsize=14)

# Add numbers on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, round(yval), ha='center', va='bottom', fontsize=12)

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set a Seaborn style
sns.set(style="whitegrid")


# Calculate class distribution for the entire dataset
full_class_distribution = y.value_counts()

# Plot the distribution
fig, ax = plt.subplots(figsize=(8, 6))

# Plot for the full dataset
colors = ['skyblue', 'lightcoral']  # Adjust colors if needed
bars = ax.bar(full_class_distribution.index.astype(str), full_class_distribution.values, color=colors)

# Set labels and title
ax.set_title('Class Distribution in the Extracted Dataset', fontsize=16)
ax.set_xlabel('LUNG_CANCER Features', fontsize=14)
ax.set_ylabel('Count', fontsize=14)

# Add numbers on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, round(yval), ha='center', va='bottom', fontsize=12)

# Display the plot
plt.show()

"""#The genetic algorithm"""

!pip install tpot

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tpot import TPOTClassifier

encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train_filtered)
y_test_encoded = encoder.transform(y_test_encoded)

X_train, X_test = X_train_filtered, X_test_scaled
y_train, y_test = y_train_encoded, y_test_encoded

# Define the feature selection and classification pipeline
pipeline = Pipeline([
    ('feature_selection', SelectKBest(score_func=chi2, k=10)),
    ('classification', SVC())
])

from tpot import TPOTClassifier

# Use TPOT to perform genetic model selection
tpot = TPOTClassifier(
    generations=10,
    population_size=20,
    scoring='accuracy',
    cv=3,
    verbosity=2,
    random_state=42,
    config_dict='TPOT light'
)
tpot.fit(X_train, y_train)

best_model = tpot.fitted_pipeline_

# Train the best model with the callbacks
best_model.fit(X_train, y_train)

import prettytable as pt

# TPOT results data
generation_data = [
    [1, 0.9920318725099602],
    [2, 0.9920318725099602],
    [3, 0.9933598937583001],
    [4, 0.9933598937583001],
    [5, 0.9933598937583001],
    [6, 0.9933598937583001],
    [7, 0.9933598937583001],
    [8, 0.9933598937583001],
    [9, 0.9933598937583001],
    [10, 0.9940239043824701]
]

best_pipeline = "KNeighborsClassifier(input_matrix, n_neighbors=5, p=1, weights=distance)"

# Create a PrettyTable instance
tpot_table = pt.PrettyTable()
tpot_table.field_names = ["Generation", "Best Internal CV Score"]
tpot_table.add_rows(generation_data)

# Add a title for the TPOT results
tpot_table.title = "TPOT Results"
tpot_table.align = "l"

# Print the PrettyTable
print(tpot_table)

# Print the Best Pipeline separately
print("\nBest Pipeline:")
print(best_pipeline)

print(best_model)

from tpot import TPOTClassifier
from sklearn.metrics import accuracy_score

# Create lists to store accuracy values and best pipelines
accuracy_list = []
best_pipelines = []

# Iterate over TPOT generations
for generation in range(1, 11):  # Specify the number of generations
    # Use TPOT to perform genetic model selection
    tpot = TPOTClassifier(
        generations=generation,
        population_size=20,
        scoring='accuracy',
        cv=3,
        verbosity=1,
        random_state=42,
        config_dict='TPOT light'
    )
    tpot.fit(X_train, y_train)

    # Print the best pipeline and its accuracy
    best_pipeline = tpot.fitted_pipeline_
    best_pipeline_str = str(best_pipeline)
    best_accuracy = accuracy_score(y_test, best_pipeline.predict(X_test))
    print(f"Generation {generation}: Best Pipeline - {best_pipeline_str}, Accuracy: {best_accuracy}")

    # Append accuracy and best pipeline to the lists
    accuracy_list.append(best_accuracy)
    best_pipelines.append(best_pipeline)

# Select the best pipeline based on the highest accuracy
best_index = accuracy_list.index(max(accuracy_list))
best_pipeline = best_pipelines[best_index]
best_accuracy = accuracy_list[best_index]

# Print the overall best pipeline and its accuracy
print("\nOverall Best Pipeline:")
print(best_pipeline)
print("Accuracy:", best_accuracy)

import matplotlib.pyplot as plt

# Create a dictionary to store the model occurrences in each generation
model_counts = {}

# Iterate over TPOT generations
for generation in range(1, 11):  # Specify the number of generations
    # Use TPOT to perform genetic model selection
    tpot = TPOTClassifier(
        generations=generation,
        population_size=20,
        scoring='accuracy',
        cv=3,
        verbosity=1,
        random_state=42,
        config_dict='TPOT light'
    )
    tpot.fit(X_train, y_train)

    # Get the best pipeline in the generation
    best_pipeline = tpot.fitted_pipeline_

    # Extract the model name from the best pipeline
    model_name = best_pipeline.steps[-1][1].__class__.__name__

    # Count the occurrences of the model in the generation
    if model_name in model_counts:
        model_counts[model_name] += 1
    else:
        model_counts[model_name] = 1

# Extract the model names and occurrence counts as separate lists
model_names = list(model_counts.keys())
occurrences = list(model_counts.values())

# Create a bar plot of the model occurrences
plt.bar(model_names, occurrences)
plt.title('Model Selection Process')
plt.xlabel('Model')
plt.ylabel('Occurrences')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create empty lists to store the model names and scores
model_names = []
scores = []

# Iterate over the evaluated individuals and store the model names and scores
for model, data in tpot.evaluated_individuals_.items():
    model_name = model.split("(")[0]  # Extract the model name from the key
    score = data['internal_cv_score']  # Get the cross-validation score from the value
    model_names.append(model_name)
    scores.append(score)

# Print the model names and scores
for model_name, score in zip(model_names, scores):
    print(f"Model: {model_name}")
    print(f"Score: {score}")
    print()

import matplotlib.pyplot as plt

# Create a bar plot of the model names and scores
plt.figure(figsize=(14, 6))
bars = plt.bar(model_names, scores, width=0.5)
plt.title('Tpot Model Scores')
plt.xlabel('Model')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.tight_layout()

# Remove colors from the bars
for bar in bars:
    bar.set_color('black')

plt.show()



y_pred = best_model.predict(X_test)

from tabulate import tabulate

# Determine the number of columns you want
num_columns = 3

# Calculate the number of rows needed
num_rows = (len(model_names) + num_columns - 1) // num_columns

# Create a list of lists containing the model names and scores
table_data = [[model_name, round(score, 3)] for model_name, score in zip(model_names, scores)]

# Create empty columns to ensure equal length of each row
while len(table_data) % num_rows != 0:
    table_data.append([])

# Reshape the table data to have multiple columns
table_data = [table_data[i:i+num_rows] for i in range(0, len(table_data), num_rows)]

# Merge the columns into a single table
merged_table_data = [sum(column_data, []) for column_data in zip(*table_data)]

# Print the table using the tabulate function
print(tabulate(merged_table_data, headers=["Model", "Score"] * num_columns, tablefmt="pretty"))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Calculate the performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print("Accuracy:", accuracy *100 )
print("Precision:", precision *100 )
print("Recall:", recall * 100 )
print("F1 Score:", f1 *100)

# Generate the confusion matrix
confusion_mat = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_mat)

import matplotlib.pyplot as plt

import seaborn as sns
# Plot the confusion matrix as a heatmap
class_names = encoder.classes_
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, cmap='Oranges', fmt='d', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()





y_pred = best_model.predict(X_test)

import matplotlib.pyplot as plt

# Define the model names and their corresponding CV scores
models = ['GaussianNB', 'RandomForestClassifier', 'XGBClassifier', 'KNeighborsClassifier', 'LinearSVC', 'ExtraTreesClassifier', 'DecisionTreeClassifier', 'BernoulliNB', 'MLPClassifier', 'GradientBoostingClassifier', 'SGDClassifier']
scores = [0.9893758300132802, 0.9926958831341302, 0.9913678618857902, 0.9933598937583001, 0.791500664010624, 0.9920318725099602, 0.9907038512616202, 0.9741035856573705, 0.9887118193891102, 0.9926958831341302, 0.791500664010624]

# Create the bar graph
plt.bar(models, scores)
plt.xlabel('Model')
plt.ylabel('Internal CV Score')
plt.title('sample of Internal CV Scores of Different Models ')
plt.xticks(rotation=90)
# Display the graph
plt.show()

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Calculate the performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print("Accuracy:", accuracy *100 )
print("Precision:", precision *100 )
print("Recall:", recall * 100 )
print("F1 Score:", f1 *100)

# Generate the confusion matrix
confusion_mat = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_mat)

import matplotlib.pyplot as plt

import seaborn as sns
# Plot the confusion matrix as a heatmap
class_names = encoder.classes_
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, cmap='Oranges', fmt='d', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""# change"""

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split

# Initialize X_train and y_train here

# Create empty lists to store the model names, best pipelines, and accuracies
model_names = []
best_pipelines = []
accuracies = []

# Define the configuration dictionary with a wider range of classifiers
custom_config_dict = {
    'sklearn.ensemble.RandomForestClassifier': {
        'n_estimators': [10, 50, 100, 200],
        'max_depth': [ 10, 20, 30],
    },
    'sklearn.ensemble.ExtraTreesClassifier': {
        'n_estimators': [10, 50, 100, 200],
        'max_depth': [ 10, 20, 30],
    },
    'sklearn.ensemble.GradientBoostingClassifier': {
        'n_estimators': [10, 50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2, 0.3],
        'max_depth': [3, 4, 5],
    },
    'sklearn.linear_model.LogisticRegression': {
        'penalty': ['l1', 'l2'],
        'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
    },
'sklearn.neighbors.KNeighborsClassifier' : {
    'n_neighbors': [71,5],
    'weights': [ 'distance'],
    'p': [1]
}

}
# Iterate over TPOT generations
for generation in range(1, 20):  # Specify the number of generations
    # Use TPOT to perform genetic model selection with custom config
    tpot = TPOTClassifier(
        generations=generation,
        population_size=20,
        scoring='accuracy',
        cv=3,
        verbosity=1,
        random_state=42,
        config_dict=custom_config_dict
    )
    tpot.fit(X_train, y_train)

    # Get the best pipeline in the generation
    best_pipeline = tpot.fitted_pipeline_

    # Extract the model name from the best pipeline
    model_name = best_pipeline.steps[-1][1].__class__.__name__

    # Evaluate the best pipeline on the test set
    y_pred = best_pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Print and store the results
    print(f"Generation {generation}: Best Pipeline - {best_pipeline}, Accuracy: {accuracy}")
    model_names.append(model_name)
    best_pipelines.append(best_pipeline)
    accuracies.append(accuracy)

# Visualize the occurrences of each model
model_counts = dict(zip(model_names, accuracies))
plt.bar(model_counts.keys(), model_counts.values())
plt.title('Model Selection Process')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Select the best pipeline based on the highest accuracy
best_index = accuracies.index(max(accuracies))
best_pipeline = best_pipelines[best_index]
best_accuracy = accuracies[best_index]

# Print the overall best pipeline and its accuracy
print("\nOverall Best Pipeline:")
print(best_pipeline)
print("Accuracy:", best_accuracy)
