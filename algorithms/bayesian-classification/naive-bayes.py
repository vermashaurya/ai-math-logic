import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_dataset():
    data = [
        {'Subject': 'Discount Offer', 'Sender': 'marketing@example.com', 'Body': 'Dear customer, we have a special discount offer for you...', 'Attachment': False, 'Label': 'Not spam'},
        {'Subject': 'Urgent Request', 'Sender': 'manager@example.com', 'Body': 'Hi, I need your help with an urgent request...', 'Attachment': False, 'Label': 'Not spam'},
        {'Subject': 'Exclusive Deal', 'Sender': 'sales@example.com', 'Body': "Don't miss out on our exclusive deal of the day...", 'Attachment': True, 'Label': 'Not spam'},
        {'Subject': 'Important Update', 'Sender': 'support@example.com', 'Body': 'We have released an important update for our software...', 'Attachment': False, 'Label': 'Not spam'},
        {'Subject': 'Claim Your Prize', 'Sender': 'winner@example.com', 'Body': 'Congratulations! You have won a prize worth $10,000...', 'Attachment': False, 'Label': 'Spam'},
        {'Subject': 'Limited Time Offer', 'Sender': 'promotions@example.com', 'Body': 'Limited time offer: Get 50% off on selected items...', 'Attachment': True, 'Label': 'Not spam'},
        {'Subject': 'Job Opportunity', 'Sender': 'careers@example.com', 'Body': 'Exciting job opportunity available at our company...', 'Attachment': True, 'Label': 'Not spam'},
        {'Subject': 'Exclusive Invitation', 'Sender': 'event@example.com', 'Body': "You're invited to an exclusive event...", 'Attachment': False, 'Label': 'Not spam'},
        {'Subject': 'Get Rich Quick', 'Sender': 'money@example.com', 'Body': 'Make money fast with our guaranteed investment scheme...', 'Attachment': False, 'Label': 'Spam'},
        {'Subject': 'Special Announcement', 'Sender': 'ceo@example.com', 'Body': 'Important announcement from the CEO...', 'Attachment': False, 'Label': 'Not spam'}
    ]
    return pd.DataFrame(data)

dataset = load_dataset()

X = dataset[['Subject', 'Sender', 'Body', 'Attachment']]
y = dataset['Label']

X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

classifier = GaussianNB()

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
