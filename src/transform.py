import pandas as pd

def transform(df):
    # standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )

    # remove missing rows based on required columns
    df = df.dropna(subset=["model_year", "electric_range"])

    # convert to numeric safely
    df["model_year"] = pd.to_numeric(df["model_year"], errors="coerce")
    df["electric_range"] = pd.to_numeric(df["electric_range"], errors="coerce")

    # drop again after conversion
    df = df.dropna(subset=["model_year", "electric_range"])

    # remove rows where electric_range = 0
    df = df[df["electric_range"] != 0]

    # remove duplicates based on dol_vehicle_id
    df = df.drop_duplicates(subset=["dol_vehicle_id"])

    # reset index
    df = df.reset_index(drop=True)

    return df