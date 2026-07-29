from sklearn.pipeline import Pipeline

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.linear_model import (
    LogisticRegression
)

from sklearn.tree import (
    DecisionTreeClassifier
)

from sklearn.svm import SVC

from sklearn.neighbors import (
    KNeighborsClassifier
)

# logistic regression 
def train_logistic_regression(
    preprocessor
):

    return Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])


# random forest
def train_random_forest(
    preprocessor
):

    return Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                random_state=42
            )
        )
    ])


# decision tree
def train_decision_tree(
    preprocessor
):

    return Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                random_state=42
            )
        )
    ])


# knn
def train_knn(
    preprocessor
):

    return Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            KNeighborsClassifier()
        )
    ])


# svm
def train_svm(
    preprocessor
):

    return Pipeline([
        ("preprocessor", preprocessor),
        (
            "classifier",
            SVC(
                probability=True
            )
        )
    ])