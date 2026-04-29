import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'Age': [35, 45, 22, 30, 40, 28, 38, 48, 50, 60],
    'Income': ['High', 'High', 'Low', 'Medium', 'Medium', 'Low', 'High', 'High', 'Low', 'Medium'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Label': ['Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes']
}

dataset = pd.DataFrame(data)

dataset_encoded = pd.get_dummies(dataset, columns=['Income', 'Gender'])

X = dataset_encoded.drop('Label', axis=1)
y = dataset_encoded['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = DecisionTreeClassifier()

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
