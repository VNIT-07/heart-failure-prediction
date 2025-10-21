🫀 Heart Failure Prediction

Imagine being able to predict if someone might face heart problems — before it happens.
That’s what this project tries to do.

Using real medical data and a bit of machine learning, this system helps detect whether a patient is at risk of heart failure.
It’s like giving doctors a digital assistant that whispers:

“Hey, this patient’s health data looks risky — take a closer look.”

🌟 What This Project Does

This system looks at different health indicators (like age, blood pressure, and ejection fraction) and predicts whether a patient is likely to experience heart failure.

It learns from real clinical records and finds hidden patterns that doctors can use to make better decisions.

Just like how you might notice that older age and high blood pressure often go together —
this model learns those patterns on its own.

🧠 How It Works (In Simple Terms)

Learn from examples – The computer studies real patient data where the outcomes (death or survival) are already known.

Understand numbers – It looks at medical values like serum creatinine, ejection fraction, and age to find risk patterns.

Make decisions – Using a Decision Tree Classifier, it figures out what combinations of values lead to higher chances of heart failure.

Predict outcomes – When you give it a new patient’s data, it says:

“Yes, this patient may be at risk.” or
“No, this patient seems safe.”


🗂 Project Files Explained
| File Name                                      | Purpose                                                              |
| :--------------------------------------------- | :------------------------------------------------------------------- |
| **heart_failure_clinical_records_dataset.csv** | The dataset containing patient details and health measurements.      |
| **HeartFailure.ipynb**                         | Jupyter Notebook where the model is trained, tested, and visualized. |
| **model.py**                                   | A simple Python script to test predictions on new data.              |
| **heart_model.pkl**                            | Saved Decision Tree model for reuse without retraining.              |
| **heart_features.pkl**                         | Stores the selected features used for predictions.                   |


💻 Model Performance
The model was trained and tested on clinical data and performed quite well.

Metric	Score
| Metric                     | Score  |
| :------------------------- | :----- |
| 🎯 **Accuracy**            | 87.88% |
| 🧩 **Precision (Class 0)** | 0.87   |
| 🧩 **Precision (Class 1)** | 0.92   |
| 🔁 **Recall (Class 0)**    | 0.97   |
| 🔁 **Recall (Class 1)**    | 0.69   |
| 📉 **R² Score**            | 0.445  |


So overall, the model can correctly identify most patients who are at risk — a strong starting point for real-world prediction.

📊 What the Model Found Important

When the Decision Tree analyzed the data, it found that some features matter more than others:

🧬 Serum Creatinine – High levels often indicate kidney strain or heart issues.

❤️ Ejection Fraction – Measures how well the heart pumps blood.

👴 Age – Older patients showed higher risk levels.

These were among the top predictors in identifying potential heart failure cases.
