from sklearn.preprocessing import LabelEncoder


def encode_diagnosis(df):

    diagnosis_encoder = LabelEncoder()

    df["diagnosis"] = diagnosis_encoder.fit_transform(
        df["diagnosis"]
    )

    return df, diagnosis_encoder


def encode_severity(df):

    severity_encoder = LabelEncoder()

    df["severity"] = severity_encoder.fit_transform(
        df["severity"]
    )

    return df, severity_encoder