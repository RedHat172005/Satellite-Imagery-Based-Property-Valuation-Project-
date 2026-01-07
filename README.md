# Satellite-Imagery-Based-Property-Valuation-Project-
This project implements a Multimodal Deep Learning Architecture to predict residential property prices. By fusing traditional tabular data (house specifications) with visual data (satellite imagery), the model achieves higher accuracy and contextual awareness than standard regression models.

🚀 Project Overview
Data Source: King County Housing Dataset + Esri World Imagery (Satellite).
Architecture: Dual-stream Fusion Model (ResNet18 + Multi-Layer Perceptron).
Target: Property price prediction on a log-transformed scale for improved stability.

📁 Repository Structure
data_fetcher.py: Python script to convert coordinates to map tiles and download satellite imagery.

preprocessing.ipynb: Data cleaning, Exploratory Data Analysis (EDA), and feature engineering.

model_training.ipynb: The core engine containing the PyTorch model definition, training loop, and Grad-CAM explainability.

23117143_final.csv: The final prediction output for the test dataset.

23117143_report.pdf: Comprehensive project report with detailed visualizations.

🧠 Methodology
1. Visual Feature Extraction (CNN)
We utilize a ResNet18 backbone (pre-trained on ImageNet) to analyze 224x224 satellite image tiles. The CNN identifies visual cues like roof size, property density, and local greenery.

2. Tabular Feature Processing (MLP)
A 3-layer Neural Network processes 17 architectural features (sqft, grade, bathrooms, etc.). All features are normalized using StandardScaler to ensure balanced gradient updates.

3. Model Fusion
The 512-dimensional vector from the CNN and the 16-dimensional vector from the MLP are concatenated into a Fusion Layer, which then passes through a final regression head to output the predicted price.

🛠️ Installation & Usage
Clone the Repo:

Bash

git clone https://github.com/your-username/your-repo-name.git
Download Images: Run the fetcher to populate the images/ folder.

Bash

python data_fetcher.py
Run Notebooks: Execute preprocessing.ipynb followed by model_training.ipynb to train the model and generate the final_predictions.csv.

📊 Key Results
Training Samples: 8,000 properties (subset chosen to prevent overfitting and ensure high generalization).

Final Loss: 0.033 (Log-MSE).

Explainability: Grad-CAM heatmaps confirm the model focuses on the primary house structure and plot size to determine value.
