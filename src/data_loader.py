import pandas as pd


def load_data(file_path):
    """
    Load malaria dataset
    """

    df = pd.read_csv(file_path)

    return df