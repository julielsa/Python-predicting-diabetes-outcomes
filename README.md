# Predicting Diabetes Outcomes

### Overview
Project aims to predict diabetes outcomes using the Pima Diabetes Database, employing Python for data preprocessing, modeling, and for exploratory data analysis and visualization. Key steps include data cleaning, feature scaling, model training, and evaluation using metrics like accuracy and AUC.
   
   Key questions:
   - Can we predict whether a patient has diabetes based on their health metrics?
   - Which health points of measure are the most telling in predicting diabetes?
   - How reliable are the predictions?

### Dataset 
Leveraged the Kaggle ['Pima Indians Diabetes Database'](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data). The dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases and it represents the information of 21 year old females of Pima heritage. The variables presented are their insulin level, BMI, age, blood pressure, pregnancies, and a target variable, outcome. 

### Analysis
1. Data Cleaning and Processing

   After downloading the dataset, below are the steps taken:
   - Replace missing values: This dataset also has '0' values under metrics like BMI that are not typical biologically.
   - Handling missing values: Using mean/median imputation will allow for missing values to be replaced with estimates.
   - Feature scaling: Ensuring all features contribute equally to the model.
   - Check for outliers
   
3. Exploratory Data Analysis
   - Histogram for Glucose Distribution:
     ![histogram.png](https://github.com/julielsa/Python-predicting-diabetes-outcomes/blob/main/histogram.png)

     Key takeaways:
     - The binary classification creates a clear baseline for model evaluation, however, it also does oversimplify the disease.
     - There are more people without diabetes than with it in this dataset, which is expected in a general population sample.
     - It is important to note that this uneven distribution means our model evalution should ensure not to be biased toward the more common outcome.
   - Corrolation Heatmap:
     ![heatmap.png](https://github.com/julielsa/Python-predicting-diabetes-outcomes/blob/main/heatmap.png)

     Key takeaways:
     - Glucose has the strongest corrolation: The data shows glucose levels have the strongest correlation with diabetes risk. 
     - Weight and age matter: Like most people know, being overweight and getting older tend to increase your chances of diabetes. This matches what the data shows us and helps explain why our model found these factors important.
     - Blood pressure less important: Based on my common knowledge, I initially thought that I would find high blood pressure to be a big warning sign for diabetes, but the data shows it's not as reliable an indicator as weight or blood sugar levels.
         
4. Modeling & Model Evaluation
   - 
   
### Insights & Conclusion

