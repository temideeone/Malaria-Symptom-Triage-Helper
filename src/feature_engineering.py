from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


def build_preprocessor(
    categorical_cols
):

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_cols
            )
        ],
        remainder="passthrough"
    )

    return preprocessor