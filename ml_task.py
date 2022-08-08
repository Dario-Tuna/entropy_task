import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import logging

"""
I have decided to use the K Nearest Neighbors method
"""

model = 'K Nearest Neighbors'
logging.basicConfig(filename="ml_result_logger.log", filemode="a", level=logging.INFO,
                    format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
car_data = pd.read_csv("car_data.csv")
print(f"basic df info:\n {car_data.info()}")
print(f"printing the head of the dataframe:\n {car_data.head()}")


car_data.replace({'Gender': {'Male': 1, 'Female': 2}}, inplace=True)
print(f"Dataframe description:\n{car_data.describe()}")
scaler = StandardScaler()
scaler.fit(car_data.drop('Purchased', axis=1))
scaled_array = scaler.transform(car_data.drop('Purchased', axis=1))
scaled_df = pd.DataFrame(scaled_array, columns=car_data.columns[:-1])
X = scaled_df
y = car_data['Purchased']

test_split_text = ['50-50', '70-30', '80-20']
test_size_array = [0.5, 0.3, 0.2]
for x in range(len(test_size_array)):
    print(x)
    print(type(x))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_array[x]) #split data to train and test

    error_rate = []
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error_rate.append(np.mean(pred_i != y_test))

    k_values = np.argmin(error_rate)+1
    knn = KNeighborsClassifier(n_neighbors=k_values)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    print(f"confusion matrix:\n {confusion_matrix(y_test, pred)}")
    print(f"Accuracy report:\n {accuracy}")
    logging.info(f"model={model}, split={test_split_text[x]}, accuracy= {accuracy}")
