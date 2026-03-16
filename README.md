<div align="center">

# 🐍 VKPyKit

**A comprehensive Python toolkit for Machine Learning and Data Science workflows**

[![PyPI Version](https://img.shields.io/pypi/v/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)
[![Python Versions](https://img.shields.io/pypi/pyversions/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)
[![License](https://img.shields.io/pypi/l/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)
[![Status](https://img.shields.io/pypi/status/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)

[![Downloads (Monthly)](https://img.shields.io/pypi/dm/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)
[![Downloads (Weekly)](https://img.shields.io/pypi/dw/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)
[![Downloads (Daily)](https://img.shields.io/pypi/dd/VKPyKit.svg)](https://pypi.python.org/pypi/VKPyKit)

[![GitHub Release](https://img.shields.io/github/release/assignarc/VKPyKit.svg)](https://github.com/assignarc/VKPyKit/releases)
[![GitHub Tag](https://img.shields.io/github/tag/assignarc/VKPyKit.svg)](https://github.com/assignarc/VKPyKit/tags)

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

VKPyKit is a production-ready Python package designed to streamline common Machine Learning and Data Science tasks. Built on top of industry-standard libraries like scikit-learn, pandas, matplotlib, seaborn, TensorFlow, and Keras, it provides convenient wrapper functions and utilities for:

- **VKPy Utilities**: Core utility functions for reproducible ML experiments including seed management
- **Exploratory Data Analysis (EDA)**: Comprehensive visualization and statistical analysis tools
- **Decision Trees (DT)**: Model training, evaluation, hyperparameter tuning, pruning, and tree visualization
- **Linear Regression (LR)**: Regression model performance assessment with multiple metrics
- **Machine Learning Models (MLM)**: General classification model performance evaluation and visualization

Instead of repeatedly writing the same boilerplate code across projects, VKPyKit packages these commonly-used functions into a reusable, well-tested library.

## ✨ Features

### 🛠️ VKPy Utilities

- **Seed Management**: Set random seeds across all major ML libraries (NumPy, TensorFlow, Keras, PyTorch)
- **Reproducibility**: Ensure consistent results across multiple runs of your experiments
- **Multi-Library Support**: Single function call to set seeds for all commonly used ML frameworks
- **CUDA Support**: Automatic configuration for GPU-based PyTorch experiments

### 📊 Exploratory Data Analysis (EDA)

- **Stacked Bar Plots**: Visualize categorical distributions with respect to target variables
- **Labeled Bar Plots**: Bar charts with percentage or count annotations
- **Distribution Analysis**: Combined histogram and boxplot visualizations
- **Outlier Detection**: Automated boxplot generation for outlier identification
- **Correlation Heatmaps**: Visualize feature correlations
- **Pair Plots**: Comprehensive pairwise relationship visualization
- **Target Distribution**: Analyze feature distributions across target classes
- **Pivot Tables**: Generate comprehensive pivot tables with multiple statistics
- **Data Overview**: Quick statistical summary and data quality assessment
- **Image Grid Display**: Plot a random sample of images from a dataset with labels

### 🌲 Decision Trees (DT)

- **Model Performance Metrics**: Comprehensive classification performance reporting
- **Confusion Matrices**: Visual confusion matrix generation with customization
- **Tree Visualization**: Render decision tree structure with optional text rules and feature importance
- **Hyperparameter Tuning**: Automated grid search for optimal decision tree parameters (returns model or full results dict)
- **Pre-Pruning**: Grid search with automated visualization and train/test evaluation
- **Post-Pruning**: Cost-complexity pruning path analysis with F1-score optimization
- **Feature Importance**: Analyze and visualize feature contributions

### 📈 Linear Regression (LR)

- **Performance Evaluation**: R², Adjusted R², RMSE, MAE, and MAPE regression metrics
- **MAPE Score**: Mean Absolute Percentage Error utility
- **Adjusted R²**: Penalized R² accounting for number of predictors

### 🤖 Machine Learning Models (MLM)

- **Model Performance Metrics**: Comprehensive classification performance reporting for any sklearn classifier
- **Confusion Matrices**: Visual confusion matrix generation with percentages and optional binary threshold conversion
- **Model Evaluation**: Accuracy, Precision, Recall, and F1-Score metrics; supports `argmax` for multi-class outputs
- **Feature Importance Visualization**: Plot and rank features by their importance scores
- **Training History Tracking**: Visualize Keras/TensorFlow model training metrics over epochs
- **End-to-End Model Execution**: Complete training, validation, and reporting pipeline for neural networks
- **Universal Compatibility**: Works with any scikit-learn classification model and TensorFlow/Keras models

## 🚀 Installation

### Using pip (Recommended)

```bash
pip install VKPyKit
```

### From Source

```bash
git clone https://github.com/assignarc/VKPyKit.git
cd VKPyKit
pip install -e .
```

### Requirements

- Python >= 3.9
- Dependencies: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `openpyxl`, `plotly`, `tensorflow`, `keras`

All dependencies will be automatically installed with the package.

## 🎯 Quick Start

```python
from VKPyKit.VKPy import *
from VKPyKit.EDA import *
from VKPyKit.DT import *
from VKPyKit.LR import *
from VKPyKit.MLM import *

# Set seeds for reproducibility across all ML libraries
VKPy.setseed(42)

# Quick EDA visualization
EDA.histogram_boxplot_all(
    data=df,
    figsize=(15, 10),
    bins=10,
    kde=True
)

# Train and evaluate a Decision Tree
DT.model_performance_classification(
    model=my_dt_classifier,
    predictors=X_test,
    expected=y_test,
    printall=True,
    title='Customer Churn Model'
)

# Evaluate any classification model
MLM.model_performance_classification(
    model=my_classifier,
    predictors=X_test,
    expected=y_test,
    printall=True,
    title='My Classification Model'
)

# Plot feature importance
MLM.plot_feature_importance(
    model=my_model,
    features=feature_names,
    numberoftopfeatures=10
)

# Evaluate a regression model
LR.model_performance_regression(
    model=my_lr_model,
    predictors=X_test,
    target=y_test
)
```

## 📚 Documentation

### VKPy Utilities

#### Seed Management for Reproducibility

Ensure consistent results across multiple runs of your ML experiments by setting random seeds for all major libraries:

```python
from VKPyKit.VKPy import *

# Set seed for reproducibility across NumPy, TensorFlow, Keras, and PyTorch
VKPy.setseed(42)

# Now all random operations will be reproducible
# This affects:
# - NumPy random operations
# - TensorFlow/Keras model initialization and training
# - PyTorch model initialization and training (including CUDA operations)
# - Python's built-in random module
```

**Benefits:**

- ✅ Reproducible experiments across different runs
- ✅ Consistent model initialization weights
- ✅ Reliable train-test splits
- ✅ Easier debugging and model comparison
- ✅ GPU operations (CUDA) are also deterministic

### Exploratory Data Analysis (EDA)

#### Histogram with Boxplot

Visualize the distribution of all numerical features in your dataset:

```python
from VKPyKit.EDA import *
import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Generate histogram and boxplot for all numerical columns
EDA.histogram_boxplot_all(
    data=df,
    figsize=(15, 10),
    bins=10,
    kde=True
)

# Generate histogram and boxplot for a single feature
EDA.histogram_boxplot(
    data=df,
    feature='age',
    figsize=(12, 7),
    kde=True,
    bins=20
)
```

#### Stacked Bar Plots

Visualize categorical variable distributions against a target:

```python
# Single stacked bar plot
EDA.barplot_stacked(
    data=df,
    predictor='category_column',
    target='target_column'
)

# Multiple stacked bar plots
EDA.barplot_stacked_all(
    data=df,
    predictors=['cat_col1', 'cat_col2', 'cat_col3'],
    target='target_column'
)
```

#### Labeled Bar Plots

```python
# Single labeled bar plot (with optional percentage display)
EDA.barplot_labeled(
    data=df,
    feature='category_column',
    percentages=True,
    category_levels=10  # show top 10 levels only
)

# Multiple labeled bar plots for a list of predictors
EDA.barplot_labeled_all(
    data=df,
    predictors=['cat_col1', 'cat_col2'],
    target='target_column'
)
```

#### Distribution Analysis for Target Variable

```python
# Analyze how a feature distributes across target classes
EDA.distribution_plot_for_target(
    data=df,
    predictor='numerical_feature',
    target='target_column',
    figsize=(12, 10)
)

# Analyze multiple features
EDA.distribution_plot_for_target_all(
    data=df,
    predictors=['feature1', 'feature2', 'feature3'],
    target='target_column',
    figsize=(12, 10)
)
```

#### Correlation Analysis

```python
# Generate correlation heatmap
EDA.heatmap_all(
    data=df,
    features=['feature1', 'feature2', 'feature3']  # Optional: specify features
)

# Generate pairplot for feature relationships
EDA.pairplot_all(
    data=df,
    features=['feature1', 'feature2', 'feature3'],
    hues=['target_column'],
    min_unique_values_for_pairplot=4,
    diagonal_plot_kind='auto'
)
```

#### Outlier Detection

```python
# Visualize outliers across all numerical features
EDA.boxplot_outliers(data=df)

# Boxplot for a dependent variable against multiple categories
EDA.boxplot_dependent_category(
    data=df,
    dependent='price',
    independent=['brand', 'category'],
    figsize=(12, 5)
)
```

#### Pivot Tables and Statistical Analysis

```python
# Generate comprehensive pivot tables with multiple statistics
EDA.pivot_table_all(
    data=df,
    predictors=['category1', 'category2'],
    target='numerical_target',
    stats=['mean', 'median', 'count', 'std'],
    figsize=(12, 10),
    chart_type='bar',  # 'bar', 'line', or None
    printall=True
)
```

#### Quick Data Overview

```python
# Get a comprehensive statistical summary and data quality check
EDA.overview(
    data=df,
    printall=True
)
# Displays: shape, data types, missing values, duplicates, basic statistics, and memory usage
```

#### Image Grid Display

```python
# Plot a sample grid of images with their labels
EDA.plot_images(
    images=image_array,   # numpy array of images
    labels=labels_df,     # DataFrame with 'Label' column
    rows=3,
    cols=4
)
```

### Decision Trees (DT)

#### Model Performance Evaluation

```python
from VKPyKit.DT import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Prepare your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate performance
DT.model_performance_classification(
    model=model,
    predictors=X_test,
    expected=y_test,
    printall=True,
    title='Decision Tree Classifier Performance'
)
```

#### Confusion Matrix Visualization

```python
# Plot confusion matrix
DT.plot_confusion_matrix(
    model=model,
    predictors=X_test,
    expected=y_test,
    title='Confusion Matrix - Decision Tree'
)
```

#### Tree Visualization

```python
# Visualize the tree structure with optional text rules + feature importance
DT.visualize_decision_tree(
    model=model,
    features=X_train.columns.tolist(),
    classes=['No', 'Yes'],
    figsize=(20, 10),
    showtext=True,        # print text rules
    showimportance=True   # plot feature importance
)
```

#### Hyperparameter Tuning

```python
# Returns best DecisionTreeClassifier model
best_model = DT.tune_decision_tree(
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test,
    max_depth_v=(2, 11, 2),           # (start, end, step)
    max_leaf_nodes_v=(10, 51, 10),
    min_samples_split_v=(10, 51, 10),
    printall=True,
    sortresultby=['F1Difference'],
    sortbyAscending=False
)

# Returns a full results dictionary (scores df, tuned model scores df, and best model)
results = DT.tune_decision_tree_results(
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test,
    max_depth_v=(2, 11, 2),
    max_leaf_nodes_v=(10, 51, 10),
    min_samples_split_v=(10, 51, 10),
    printall=True,
    sortresultby=['F1Difference'],
    sortbyAscending=False,
    metrictooptimize='F1Difference'   # 'Accuracy', 'Recall', 'Precision', 'F1', 'F1Difference', 'RecallDifference'
)

print(results['scores'])            # All combinations
print(results['tuned_model_scores']) # Best combination
best_model = results['model']
```

#### Pre-Pruning

```python
# Run grid search, visualize best tree, and evaluate on train/test
prepruning_results = DT.prepruning_nodes_samples_split(
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test,
    max_depth_v=(2, 9, 2),
    max_leaf_nodes_v=(50, 250, 50),
    min_samples_split_v=(10, 70, 10),
    printall=True,
    sortresultby='F1',
    sortbyAscending=False
)

model = prepruning_results['model']
train_perf = prepruning_results['prepruning_train_perf']
test_perf  = prepruning_results['prepruning_test_perf']
```

#### Post-Pruning (Cost-Complexity)

```python
# Analyze the cost-complexity path and select the best alpha
postpruning_results = DT.postpruning_cost_complexity(
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test,
    printall=True,
    figsize=(10, 6)
)

model = postpruning_results['model']
train_perf = postpruning_results['postpruning_train_perf']
test_perf  = postpruning_results['postpruning_test_perf']
```

### Linear Regression (LR)

#### Evaluate a Regression Model

```python
from VKPyKit.LR import *

# Computer comprehensive regression metrics (RMSE, MAE, MAPE, R², Adj R²)
perf_df = LR.model_performance_regression(
    model=my_lr_model,
    predictors=X_test,
    target=y_test
)
print(perf_df)
# Returns DataFrame with: RMSE, MAE, MAPE, R-squared, Adj R-squared

# Utility: MAPE score
mape = LR.mape_score(targets=y_test, predictions=y_pred)

# Utility: Adjusted R² score
adj_r2 = LR.adj_r2_score(predictors=X_test, targets=y_test, predictions=y_pred)
```

### Machine Learning Models (MLM)

#### Evaluate Any Classification Model

The MLM module works with any scikit-learn classifier (Random Forest, SVM, Logistic Regression, etc.):

```python
from VKPyKit.MLM import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Prepare your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train any classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate performance with comprehensive metrics
MLM.model_performance_classification(
    model=model,
    predictors=X_test,
    expected=y_test,
    threshold=0.5,           # threshold for binary classification
    score_average='binary',  # 'binary', 'macro', 'weighted', etc.
    printall=True,
    title='Random Forest Classifier',
    idmax=False              # set True for multi-class models using argmax
)
```

#### Confusion Matrix for Any Classifier

```python
# Plot confusion matrix with percentages
MLM.plot_confusion_matrix(
    model=model,
    predictors=X_test,
    expected=y_test,
    convert_pred_to_binary=False,  # set True to threshold continuous predictions
    threshold=0.5,
    title='Random Forest - Confusion Matrix'
)
```

#### Feature Importance Visualization

```python
# Plot feature importance for tree-based models
MLM.plot_feature_importance(
    model=model,
    features=X_train.columns.tolist(),
    figsize=(10, 6),
    numberoftopfeatures=15,  # Show top 15 features
    title='Random Forest Feature Importance',
    ignoreZeroImportance=True  # Hide features with zero importance
)
```

#### Training History for Neural Networks

```python
from tensorflow import keras

# Train a Keras model
model = keras.Sequential([...])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50)

# Plot all metrics in training history
MLM.model_history_plot(
    history=history,
    title='Neural Network Training'
)

# Plot a specific metric only
MLM.model_history_plot(
    history=history,
    plot_metric='accuracy',
    title='Model Accuracy Over Epochs'
)
```

#### End-to-End Model Execution

```python
import tensorflow as tf
from tensorflow import keras

# Prepare data dictionary
data = {
    "X_train": X_train,
    "y_train": y_train,
    "X_val": X_val,
    "y_val": y_val
}

# Define your model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Execute complete training and evaluation pipeline
results = MLM.execute_model(
    model_in=model,
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    model_name='Binary Classifier',
    data=data,
    class_weights={0: 1, 1: 2},  # Handle class imbalance
    loss_type=keras.losses.BinaryCrossentropy(),
    optmization_metrics=[keras.metrics.BinaryAccuracy(), keras.metrics.Recall()],
    threshold=0.5,
    target_names=['Class 0', 'Class 1'],
    epochs=50,
    batch_size=32,
    verbose=1,
    print_model_summary=True,
    activation='relu'
)

# Results DataFrame contains comprehensive metrics
print(results[['ModelName', 'Validation_Accuracy', 'Validation_F1Score']])
```

## 🛠️ API Reference

### VKPy Class

| Method          | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| `setseed(seed)` | Set random seeds across NumPy, TensorFlow, Keras, and PyTorch |

### EDA Class

| Method                               | Description                                               |
| ------------------------------------ | --------------------------------------------------------- |
| `histogram_boxplot()`                | Combined histogram and boxplot for a single feature       |
| `histogram_boxplot_all()`            | Combined histogram and boxplot for all numerical features |
| `barplot_stacked()`                  | Stacked bar chart for a single categorical variable       |
| `barplot_stacked_all()`              | Multiple stacked bar charts for a list of predictors      |
| `barplot_labeled()`                  | Bar plot with count/percentage labels for a single feature|
| `barplot_labeled_all()`              | Labeled bar plots for a list of categorical predictors    |
| `distribution_plot_for_target()`     | Distribution analysis across target classes (single)      |
| `distribution_plot_for_target_all()` | Distribution analysis across target classes (multiple)    |
| `boxplot_outliers()`                 | Outlier detection boxplots for all numerical features     |
| `boxplot_dependent_category()`       | Boxplot for a dependent variable vs. category features    |
| `heatmap_all()`                      | Correlation heatmap                                       |
| `pairplot_all()`                     | Pairwise feature relationship plots                       |
| `pivot_table_all()`                  | Generate pivot tables with multiple statistics            |
| `overview()`                         | Quick statistical summary and data quality check          |
| `plot_images()`                      | Display a random sample grid of images with labels        |

### DT Class

| Method                               | Description                                                              |
| ------------------------------------ | ------------------------------------------------------------------------ |
| `model_performance_classification()` | Comprehensive performance metrics (Accuracy, Recall, Precision, F1)      |
| `plot_confusion_matrix()`            | Visualize confusion matrix with counts and percentages                   |
| `visualize_decision_tree()`          | Render tree structure; optionally show text rules and feature importance  |
| `tune_decision_tree()`               | Grid search tuning — returns best `DecisionTreeClassifier` model         |
| `tune_decision_tree_results()`       | Grid search tuning — returns dict of scores, tuned scores, and model     |
| `prepruning_nodes_samples_split()`   | Pre-pruning via grid search with full train/test evaluation              |
| `postpruning_cost_complexity()`      | Post-pruning via cost-complexity path; selects best alpha by test F1     |
| `plot_feature_importance()`          | Visualize feature importance scores                                      |

### LR Class

| Method                        | Description                                              |
| ----------------------------- | -------------------------------------------------------- |
| `model_performance_regression()` | Compute RMSE, MAE, MAPE, R², and Adjusted R² metrics |
| `mape_score()`                | Compute Mean Absolute Percentage Error                   |
| `adj_r2_score()`              | Compute Adjusted R² given predictors, targets, preds     |

### MLM Class

| Method                               | Description                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| `model_performance_classification()` | Comprehensive performance metrics for any classifier; supports threshold and argmax |
| `plot_confusion_matrix()`            | Visualize confusion matrix with percentages; supports binary threshold conversion   |
| `plot_feature_importance()`          | Plot and display feature importance rankings with optional filtering                |
| `model_history_plot()`               | Visualize Keras/TensorFlow training history (loss, accuracy, custom metrics)        |
| `execute_model()`                    | Complete end-to-end training, validation, and evaluation pipeline for Keras         |

## 🧪 Testing

VKPyKit includes a comprehensive test suite to ensure code quality and reliability. The test suite covers all major modules:

- **EDA Module Tests** (`tests/test_EDA.py`): Tests for all exploratory data analysis functions
- **DT Module Tests** (`tests/test_DT.py`): Tests for decision tree utilities
- **LR Module Tests** (`tests/test_LR.py`): Tests for linear regression functions
- **MLM Module Tests** (`tests/test_MLM.py`): Tests for machine learning model evaluation

### Running Tests

```bash
# Install test dependencies
pip install VKPyKit[test]

# Run all tests
pytest

# Run tests with coverage report
pytest --cov=VKPyKit
```

The test suite uses synthetic data generated via `conftest.py` to ensure reproducible and reliable testing.

## 🤝 Contributing

Contributions are welcome! If you have additional utility functions or improvements, please contribute to the project.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Reporting Issues

Found a bug or have a feature request? Please open an issue on [GitHub Issues](https://github.com/assignarc/VKPyKit/issues).

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vishal Khapre**

- GitHub: [@assignarc](https://github.com/assignarc)
- PyPI: [VKPyKit](https://pypi.org/project/VKPyKit/)

## 🌟 Acknowledgments

Built with:

- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/)

---

<div align="center">

**[⬆ Back to Top](#-vkpykit)**

Made by [Vishal Khapre](https://github.com/assignarc)

If you find VKPyKit useful, please consider giving it a ⭐ on [GitHub](https://github.com/assignarc/VKPyKit)!

</div>
