import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the CSV file
data = pd.read_csv('/home/ali/Desktop/smje4383/UCI_Credit_Card.csv')

# Display the first few rows of data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Get Target data
y = data['default.payment.next.month']

# Load X Variables into a Pandas DataFrame with selected columns
X = data.drop(['ID', 'default.payment.next.month'], axis=1)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the SVM model
SVM_Model = SVC(gamma='auto')
SVM_Model.fit(X_train, y_train)

# Make predictions and evaluate the model on the test set
y_pred = SVM_Model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy on test data: {accuracy:.3f}')
