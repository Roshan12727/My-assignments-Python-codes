import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import os

# Create a new notebook
nb = new_notebook()

# 1. Title
nb.cells.append(new_markdown_cell("# Bike Sharing Rental Demand Prediction\nThis notebook contains the complete end-to-end process from Data Cleaning to Model Enhancement."))

# 2. EDA & Cleaning
nb.cells.append(new_markdown_cell("## 1. Exploratory Data Analysis & Cleaning\nIn this step, we handle missing values, correct data types, and prepare the dataset."))
with open('eda_analysis_v2.py', 'r', encoding='utf-8') as f:
    nb.cells.append(new_code_cell(f.read().replace("matplotlib.use('Agg')", "# matplotlib.use('Agg')")))

# 3. Visualizations
nb.cells.append(new_markdown_cell("## 2. Data Visualization\nVisualizing patterns in demand across different metrics."))
with open('generate_ppt_images.py', 'r', encoding='utf-8') as f:
     nb.cells.append(new_code_cell(f.read().replace("matplotlib.use('Agg')", "# matplotlib.use('Agg')")))

# 4. Feature Engineering
nb.cells.append(new_markdown_cell("## 3. Feature Engineering\nTransforming time variables into cyclic features and encoding categorical data."))
with open('feature_engineering_v2.py', 'r', encoding='utf-8') as f:
    nb.cells.append(new_code_cell(f.read().replace("matplotlib.use('Agg')", "# matplotlib.use('Agg')")))

# 5. Model Building
nb.cells.append(new_markdown_cell("## 4. Model Building\nComparing Decision Tree, Random Forest, and Gradient Boosting."))
with open('model_building.py', 'r', encoding='utf-8') as f:
    nb.cells.append(new_code_cell(f.read().replace("matplotlib.use('Agg')", "# matplotlib.use('Agg')")))

# 6. Hyperparameter Tuning
nb.cells.append(new_markdown_cell("## 5. Hyperparameter Tuning\nOptimizing the Random Forest model for better accuracy."))
with open('hyperparameter_tuning.py', 'r', encoding='utf-8') as f:
    nb.cells.append(new_code_cell(f.read().replace("matplotlib.use('Agg')", "# matplotlib.use('Agg')")))

# Save
with open('Bike_Sharing_Full_Process.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Master Notebook 'Bike_Sharing_Full_Process.ipynb' created.")
