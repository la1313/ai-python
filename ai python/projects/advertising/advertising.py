import csv
import random

#import modules
from sklearn import svm
from sklearn import linear_model
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# TODO: select one model
# model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()
# model = LogisticRegression()

# Read data in from file
with open("advertising.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        # TODO: add evidence to data collection. 
        # After you add code, you need to remvoe pass statement
        pass


# TODO: store evidence in evidence variable, labels in labels variable.
evidence = []
labels = []

# TODO: Separate data into training and testing groups
# use 0.4 as test size 
# X_training, X_testing, y_training, y_testing   

# TODO: Fit model


# TODO: Make predictions on the testing set
# predictions 

# Compute how well we performed
correct = (y_testing == predictions).sum()
incorrect = (y_testing != predictions).sum()
total = len(predictions)

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")