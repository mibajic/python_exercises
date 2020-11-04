import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def source_data():
    data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/'
        'balance-scale/balance-scale.data',
        sep=',', header=None)

    print("Number of rows is: ", len(data))
    print("Number of columns is: ", len(data.columns))
    print(data.head(5))
    return data


def split_data(data):
    # separating attributes and target variable
    x = data.values[:, 1:5]
    # x = x.astype('str')
    y = data.values[:, 0]
    # y = y.astype('str')
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=100)

    return x, y, x_train, x_test, y_train, y_test


def gini_index_training(x_train, x_test, y_train):
    dt = DecisionTreeClassifier(criterion="gini",
                                random_state=100,
                                max_depth=3,
                                min_samples_leaf=5)
    dt.fit(x_train, y_train)
    return dt


def prediction(x_test, classification_object):
    y_pred = classification_object.predict(x_test)
    print("Predicted values: ", y_pred)
    return y_pred


def calculation_accuracy(y_test, y_pred):
    result = confusion_matrix(y_test, y_pred)
    print("Confusion matrix: ", result)
    classification = classification_report(y_test, y_pred)
    print("Clarification: ", classification)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy)


def main():
    balance_data = source_data()
    x, y, x_train, x_test, y_train, y_test = split_data(balance_data)
    dt = gini_index_training(x_train, x_test, y_train)

    y_pred_gini = prediction(x_test, dt)
    calculation_accuracy(y_test, y_pred_gini)

if __name__ == "__main__":
    main()
