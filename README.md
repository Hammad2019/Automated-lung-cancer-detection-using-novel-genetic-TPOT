Automated Lung Cancer Detection Using Novel Genetic TPOT Feature Optimization with Deep Learning Techniques

Overview

This repository contains the implementation of our research paper:
"Automated Lung Cancer Detection Using Novel Genetic TPOT Feature Optimization with Deep Learning Techniques," published in Results in Engineering (Elsevier).

Summary

Lung cancer is one of the leading causes of cancer-related deaths worldwide. This project presents a cutting-edge methodology for early and accurate lung cancer detection by leveraging deep learning and advanced feature optimization techniques. Key highlights include:

    Utilizing both chest X-ray and CT scan images from Kaggle datasets.
    Employing genetic algorithms with TPOT for feature selection and model optimization.
    Achieving high accuracy across all models:
        Chest X-ray Model: 95.47%
        CT Model: 98.70%
        Combined Model: 98.93%

Features and Workflow
Data Preprocessing

    Load Data: Load the combined_features.csv file containing preprocessed features.

    Feature and Label Separation: Separate the features (X) and labels (y) for model training.

    Analyze Data: Obtain the number of columns and prepare data for merging.

    Label Extraction and Transformation:
        Extract labels from chest_df.
        Convert the values into the desired format.
        Remove the existing 'labels' column and add the converted labels as a new column.

    Merge DataFrames: Combine xray_df and chest_df to form the final dataset.

Model Training
Train-Test Split

    Split the dataset into training and testing sets to ensure robust evaluation.

Genetic Algorithm Optimization

    Define a feature selection and classification pipeline.
    Use TPOT to perform automated genetic optimization for model selection.
    Train the best-selected model with callbacks for enhanced performance monitoring.

Model Evaluation

    Calculate and report performance metrics:
        Accuracy
        Precision
        Recall
        F1 Score

Results

    Chest X-ray Model: Achieved 95.47% accuracy.
    CT Scan Model: Achieved 98.70% accuracy.
    Combined Model: Achieved 98.93% accuracy.

Repository Structure

├── data/  
│   ├── combined_features.csv  
│   ├── xray_data.csv  
│   └── chest_data.csv  
├── scripts/  
│   ├── preprocessing.py       # Data loading and preprocessing scripts  
│   ├── feature_selection.py   # Genetic algorithm and TPOT feature selection  
│   ├── model_training.py      # Deep learning model training pipeline  
│   ├── evaluation.py          # Performance evaluation metrics  
│   └── utils.py               # Utility functions  
├── README.md                  # Project overview and instructions  
└── requirements.txt           # Required Python packages  


Citation

If you find this repository useful, please cite the paper:

    Authors: Mohamed Hammad, Mohammed ElAffendi, Muhammad Asim, Ahmed A Abd El-Latif, Radwa Hashiesh.
    Title: Automated Lung Cancer Detection Using Novel Genetic TPOT Feature Optimization with Deep Learning Techniques
    Journal: Results in Engineering (Elsevier)
    DOI: (https://doi.org/10.1016/j.rineng.2024.103448)
