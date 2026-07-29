import pandas as pd

def feature_importance(
    model,
    feature_names
):

    classifier = model.named_steps[
        "classifier"
    ]

    importance_df = pd.DataFrame({

        "feature":
        feature_names,

        "importance":
        classifier.feature_importances_

    })

    return importance_df.sort_values(
        "importance",
        ascending=False
    )